import pyodbc

class AutomatedDB:
    def __init__(self, server, database, driver='{SQL Server}'):
        self.server = server
        self.database = database
        self.driver = driver
        self.conn = None
        self.cursor = None

    def connect(self):
        # Connect to SQL Server
        self.conn = pyodbc.connect(
            f'Driver={self.driver};'
            f'Server={self.server};'
            f'Database={self.database};'
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()
        print("✅ Connection & cursor ready!")

    def create_table(self, table_name):
        # Create a simple table dynamically
        query = f"""
        CREATE TABLE {table_name} (
            ID INT PRIMARY KEY,
            Name NVARCHAR(100),
            Age INT
        )
        """
        self.cursor.execute(query)
        self.conn.commit()
        print(f"✅ Table '{table_name}' created successfully!")

    def close(self):
        if self.conn:
            self.conn.close()
            print("🔒 Connection closed.")


# ---------- Example Usage ----------
if __name__ == "__main__":
    db = AutomatedDB(server='localhost', database='TestDB')
    db.connect()
    db.create_table("Employees")
    db.close()
