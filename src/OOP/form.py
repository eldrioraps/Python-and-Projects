import streamlit as st
import pyodbc

# ---------------- Existing Classes (unchanged) ----------------
class GeneralInfo:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def prettify_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Address": self.address
        }


class Employee(GeneralInfo):
    def __init__(self, name, age, gender, address, salary, designation):
        super().__init__(name, age, gender, address)
        self.salary = salary
        self.designation = designation

    def prettify_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Address": self.address,
            "Salary": self.salary,
            "Designation": self.designation
        }


class Customer(GeneralInfo):
    def __init__(self, name, age, gender, address, email, phone):
        super().__init__(name, age, gender, address)
        self.email = email
        self.phone = phone

    def prettify_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Address": self.address,
            "Email": self.email,
            "Phone": self.phone
        }


class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=localhost;"
            "DATABASE=TestDB;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

# ---------------- Streamlit UI ----------------
st.title("👩‍💼 Genral Info Entry")

st.write("Enter employee details to insert into the SQL Server table:")

with st.form("emp_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    gender = st.selectbox("Gender", ["M", "F"])
    address = st.text_input("Address")
    salary = st.number_input("Salary", min_value=0.0, step=500.0)
    designation = st.text_input("Designation")

    submitted = st.form_submit_button("Submit")

if submitted:
    try:
        # Create Employee object
        emp = Employee(name, age, gender, address, salary, designation)

        # Prepare INSERT query safely
        insert_query = f"""
        INSERT INTO TEST_EMP (NAME, AGE, GENDER, ADDRESS, SALARY, DESIGNATION)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        db = Database()
        db.cursor.execute(insert_query, (emp.name, emp.age, emp.gender, emp.address, emp.salary, emp.designation))
        db.conn.commit()
        db.close()

        st.success(f"✅ Employee '{emp.name}' inserted successfully!")
    except Exception as e:
        st.error(f"❌ Error inserting data: {e}")
