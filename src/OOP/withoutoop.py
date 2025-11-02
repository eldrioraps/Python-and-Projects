import pyodbc

# Database connection
conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=localhost;"  
    "DATABASE=TestDB;"
    "Trusted_Connection=yes;"  
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Non-OOP function to add a product
def add_product(product_id, name, product_type, base_price, stock, warranty_years=None, size=None):
    try:
        # Direct SQL insert
        cursor.execute("""
            INSERT INTO Products (ProductID, Name, Type, BasePrice, Stock, WarrantyYears, Size)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product_id, name, product_type, base_price, stock, warranty_years, size))
        conn.commit()
        return f"Added {name} to database"
    except Exception as e:
        return f"Error: {str(e)}"

# Simulate frontend sending product data
print("Non-OOP: Adding products...")
print(add_product("E001", "Laptop", "Electronics", 1000.00, 5, warranty_years=2))
print(add_product("C001", "T-Shirt", "Clothing", 20.00, 100, size="M"))

# Display products
cursor.execute("SELECT * FROM Products")
print("\nProducts in Database:")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()