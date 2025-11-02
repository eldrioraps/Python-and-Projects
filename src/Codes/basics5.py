import pyodbc

# ==============================
# 👨‍💼 Parent Class
# ==============================
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")


# ==============================
# 👩‍💻 Child Class (Inherits Employee)
# ==============================
class EmployeeDetail(Employee):
    def __init__(self, name, age, gender, address):
        super().__init__(name)  # ✅ Calls parent constructor
        self.age = age
        self.gender = gender
        self.address = address

    def show_details(self):
        print(f"Employee: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}")


# ==============================
# ✅ Validation Class
# ==============================
class EmpValidation:
    @staticmethod
    def validate_age(age):
        """
        Validates if employee age is between 18 and 60
        """
        if age < 18 or age > 60:  # ✅ FIXED: use logical 'or' not '|'
            print("❌ Age must be between 18 and 60")
            return False
        return True


# ==============================
# 🗄️ Database Connection Class
# ==============================
class DBConnection:
    def __init__(self):
        try:
            # ✅ Correct connection string
            self.conn = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=localhost;'
                'Database=testDB;'
                'Trusted_Connection=yes;'
            )
            self.cursor = self.conn.cursor()
            print("✅ Database connection established successfully!")
        except pyodbc.Error as e:
            print("❌ Failed to connect to database:", e)

    def insert_employee(self, emp: EmployeeDetail):
        """
        Inserts employee details into emp_test table
        """
        try:
            # ✅ Validate before insert
            if EmpValidation.validate_age(emp.age):
                query = """
                INSERT INTO emp_test (Name, Age, Gender, Address)
                VALUES (?, ?, ?, ?)
                """
                self.cursor.execute(query, (emp.name, emp.age, emp.gender, emp.address))
                self.conn.commit()
                print("✅ Employee inserted successfully!")
            else:
                print("⚠️ Employee not inserted due to failed validation.")

        except pyodbc.Error as e:
            print("❌ Database error:", e)

        finally:
            self.cursor.close()
            self.conn.close()
            print("🔒 Database connection closed.")


# ==============================
# 🚀 Execution Flow
# ==============================
if __name__ == "__main__":
    # Step 1: Create Employee object
    emp1 = EmployeeDetail("Ravi", 68, "M", "Noida, UP, India")

    # Step 2: Show Employee details
    emp1.show_details()

    # Step 3: Insert into Database
    db = DBConnection()
    db.insert_employee(emp1)
