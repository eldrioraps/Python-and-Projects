import json
import pyodbc


class JsonPrettify:
    def __init__(self, path, server, database, table, username=None, password=None):
        self.path = path
        self.server = server
        self.database = database
        self.table = table
        self.username = username
        self.password = password
        self.parsed_json = []

    def input_json(self):
        """Read and parse JSON lines file"""
        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        self.parsed_json.append(json.loads(line))
                    except json.JSONDecodeError as e:
                        print(f"Error decoding line: {e}")

    def prettify_json(self):
        """Convert JSON lines into a structured list of dicts"""
        prettified = []
        for item in self.parsed_json:
            prettified.append({
                "timestamp": item.get("timestamp"),
                "level": item.get("level"),
                "service": item.get("service"),
                "message": item.get("message"),
                "user_id": item.get("user_id")
            })
        return prettified

    def show(self, limit=5):
        """Pretty print first few entries"""
        print(json.dumps(self.parsed_json[:limit], indent=4))

    def connect_sql(self):
        """Establish connection to SQL Server"""
        if self.username and self.password:
            conn_str = (
                f"DRIVER={{SQL Server}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password}"
            )
        else:
            # For Windows Authentication
            conn_str = (
                f"DRIVER={{SQL Server}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"Trusted_Connection=yes;"
            )
        return pyodbc.connect(conn_str)

    def send_to_sql(self):
        """Insert prettified JSON data into SQL Server table"""
        conn = self.connect_sql()
        cursor = conn.cursor()

        prettified_data = self.prettify_json()

        # Make sure the table exists:
        create_table_query = f"""
        IF OBJECT_ID('{self.table}', 'U') IS NULL
        CREATE TABLE {self.table} (
            id INT IDENTITY(1,1) PRIMARY KEY,
            timestamp NVARCHAR(50),
            level NVARCHAR(50),
            service NVARCHAR(100),
            message NVARCHAR(MAX),
            user_id NVARCHAR(50)
        )
        """
        cursor.execute(create_table_query)
        conn.commit()

        # Insert rows
        for row in prettified_data:
            cursor.execute(f"""
                INSERT INTO {self.table} (timestamp, level, service, message, user_id)
                VALUES (?, ?, ?, ?, ?)
            """, row["timestamp"], row["level"], row["service"], row["message"], row["user_id"])

        conn.commit()
        conn.close()
        print(f"✅ Successfully inserted {len(prettified_data)} records into {self.table}")


# ----------------------------
# Example usage
# ----------------------------

if __name__ == "__main__":
    path = r"C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Projects\Batch\src\Libraries\jsonparsing\log.jsonl"

    jp = JsonPrettify(
        path=path,
        server="localhost",       # or your server name
        database="TestDB",         # your DB name
        table="LogTable",         # your table name
        username=None,            # optional
        password=None             # optional
    )

    jp.input_json()
    jp.show()
    jp.send_to_sql()
