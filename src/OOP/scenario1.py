from abc import ABC, abstractmethod
# from withoop import Database
import pyodbc

class Person(ABC):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establishes a database connection"""
        try:
            self.conn = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=localhost;"
                "Database=TestDB;"
                "Trusted_Connection=yes;"
            )
            self.cursor = self.conn.cursor()
            print("Database connection established.")
        except Exception as e:
            print("Connection failed:", e)

    def disconnect(self):
        """Closes the connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Connection closed.")

    @abstractmethod
    def perform_task(self):
        """Abstract method for subclasses"""
        pass
    @abstractmethod
    def validation(self):
        """Abstract method for subclasses"""
        pass


class Customer(Person):
    def __init__(self, name, email, phone, person_type):
        super().__init__(name, email, phone)
        self.person_type = person_type

    def create_table_if_not_exists(self):
        """Create table if it doesn’t exist"""
        query = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Customer' AND xtype='U')
        CREATE TABLE Customer (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(250),
            email VARCHAR(250),
            phone VARCHAR(50),
            person_type VARCHAR(100)
        )
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Customer table checked/created successfully.")
        except Exception as e:
            print("Error creating table:", e)

    def validation(self):
        print("validation Successful")

    def insert_customer(self):
        """Insert a new customer record"""
        query = "INSERT INTO Customer (name, email, phone, person_type) VALUES (?, ?, ?, ?)"
        try:
            self.cursor.execute(query, (self.name, self.email, self.phone, self.person_type))
            self.conn.commit()
            print("Customer inserted successfully.")
        except Exception as e:
            print("Error inserting customer:", e)

    def perform_task(self):
        """Implements abstract method"""
        print(f"Performing task for customer: {self.name}")

    

class Employee(Person):
    def __init__(self, name, email, phone, Employee_type,Experience,project):
        super().__init__(name, email, phone)
        self.Employee_type = Employee_type
        self.Experience=Experience
        self.project=project

    def create_table_if_not_exists(self):
        """Create table if it doesn’t exist"""
        query = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Employee' AND xtype='U')
        CREATE TABLE Employee (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(250),
            email VARCHAR(250),
            phone VARCHAR(50),
            employee_type VARCHAR(100),
            experience varchar(250),
            project varchar(250)
        )
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Employee table checked/created successfully.")
        except Exception as e:
            print("Error creating table:", e)

    def validation(self):
        print("validation Successful")

    def insert_customer(self):
        """Insert a new customer record"""
        query = "INSERT INTO Employee (name, email, phone,Employee_type,Experience,project) VALUES (?, ?, ?, ?,?,?)"
        try:
            self.cursor.execute(query, (self.name, self.email, self.phone, self.Employee_type,self.Experience,self.project))
            self.conn.commit()
            print("Employee inserted successfully.")
        except Exception as e:
            print("Error inserting customer:", e)

    def perform_task(self):
        """Implements abstract method"""
        print(f"Performing task for Employee: {self.name}")

# Example usage
if __name__ == "__main__":
    emp = Employee("John Doe", "john@example.com", "1234567890", "L1","2 years","SQL development")
    emp.connect()
    emp.create_table_if_not_exists()
    emp.validation()
    emp.insert_customer()
    emp.disconnect()

# if __name__ == "__main__":
#     cust = Customer("John Doe", "john@example.com", "1234567890", "Premium")
#     cust.connect()
#     cust.create_table_if_not_exists()
#     cust.insert_customer()
#     cust.disconnect()