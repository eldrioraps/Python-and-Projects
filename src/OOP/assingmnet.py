import pyodbc
class GeneralInfo:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def prettify_info(self):
        return {"Name":self.name,"Age":self.age,"Gender":self.gender,"Address":self.address}
    
class Employee(GeneralInfo):
    def __init__(self,name,age,gender,address,salary,designation):
        super().__init__(name,age,gender,address)
        self.salary=salary
        self.designation=designation
    def prettify_info(self):
        return {"Name":self.name,"Age":self.age,"Gender":self.gender,"Address":self.address,
                "Salary":self.salary,"Designation":self.designation}
    
class Customer(GeneralInfo):
    def __init__(self,name,age,gender,address,email,phone):
        super().__init__(name,age,gender,address)
        self.email=email
        self.phone=phone
    def prettify_info(self):
        return {"Name":self.name,"Age":self.age,"Gender":self.gender,"Address":self.address,
                "Email":self.email,"Phone":self.phone}

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



employee_table='CREATE TABLE TEST_EMP(NAME VARCHAR(250),AGE FLOAT,GENDER CHAR(2),' \
'ADDRESS VARCHAR(250),SALARY FLOAT,DESIGNATION VARCHAR(250))'


employee_table='CREATE TABLE TEST_EMP(NAME VARCHAR(250),AGE FLOAT,GENDER CHAR(2),' \
'ADDRESS VARCHAR(250),SALARY FLOAT,DESIGNATION VARCHAR(250))'

employee1=Employee('Priya','25','F','Noida',1000,"project_Manager")
# print(employee1.name)
employee_insert=f"INSERT INTO TEST_EMP VALUES('{employee1.name}','{employee1.age}','{employee1.gender}','{employee1.address}','{employee1.salary}','{employee1.designation}')"
# print(employee_insert)
db = Database()
# db.execute(employee_table)
db.execute(employee_insert)
db.close()

    
# person1=GeneralInfo('Priya','25','F','Noida')

# customer1=Customer('Priya','25','F','Noida','priya@gmail.com',"5555777788")
# print(person1.prettify_info())
# print(employee1.prettify_info())
# print(customer1.prettify_info())
# print(person1.name)
# print(person1.address)