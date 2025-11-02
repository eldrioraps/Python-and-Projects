import pyodbc
from abc import ABC, abstractmethod

# Database connection class (Encapsulation)
class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=localhost;" 
            "DATABASE=TestDB;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

# Abstraction: Product interface
class Product(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def save_to_db(self, db):
        pass

# Encapsulation: Base product class
class BaseProduct(Product):
    def __init__(self, product_id, name, base_price, stock):
        self._product_id = product_id
        self._name = name
        self._base_price = base_price
        self._stock = stock

    @property
    def name(self):
        return self._name

    @property
    def stock(self):
        return self._stock

    def reduce_stock(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
            return True
        return False

# Inheritance: Electronics product
class Electronics(BaseProduct):
    def __init__(self, product_id, name, base_price, stock, warranty_years):
        super().__init__(product_id, name, base_price, stock)
        self._warranty_years = warranty_years

    def get_details(self):
        return f"{self._name} (Electronics), Price: ${self._base_price}, Warranty: {self._warranty_years} years, Stock: {self._stock}"

    def calculate_price(self):
        discount = 0.1 if self._base_price > 500 else 0
        return self._base_price * (1 - discount)

    def save_to_db(self, db):
        db.execute("""
            INSERT INTO Products (ProductID, Name, Type, BasePrice, Stock, WarrantyYears)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self._product_id, self._name, "Electronics", self._base_price, self._stock, self._warranty_years))

# Inheritance: Clothing product
class Clothing(BaseProduct):
    def __init__(self, product_id, name, base_price, stock, size):
        super().__init__(product_id, name, base_price, stock)
        self._size = size

    def get_details(self):
        return f"{self._name} (Clothing), Price: ${self._base_price}, Size: {self._size}, Stock: {self._stock}"

    def calculate_price(self):
        return self._base_price * 0.8

    def save_to_db(self, db):
        db.execute("""
            INSERT INTO Products (ProductID, Name, Type, BasePrice, Stock, Size)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self._product_id, self._name, "Clothing", self._base_price, self._stock, self._size))

# E-Commerce System
class ECommerceSystem:
    def __init__(self):
        self._db = Database()
        self._products = []

    def add_product(self, product):
        product.save_to_db(self._db)
        self._products.append(product)

    def display_products(self):
        return "\n".join(product.get_details() for product in self._products)

    def close_db(self):
        self._db.close()

# Demo
if __name__ == "__main__":
    shop = ECommerceSystem()

    # Create products
    laptop = Electronics("E001", "Laptop", 1000.00, 5, 2)
    tshirt = Clothing("C001", "T-Shirt", 20.00, 100, "M")

    # Add to system and database
    print("OOP: Adding products...")
    shop.add_product(laptop)
    shop.add_product(tshirt)

    # Display products from system
    print("\nProduct Catalog:")
    print(shop.display_products())

    # Verify database contents
    print("\nProducts in Database:")
    for row in shop._db.fetch_all("SELECT * FROM Products"):
        print(row)

    # Close connection
    shop.close_db()