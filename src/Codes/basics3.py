data='''
# comprehension: these small block of code which helps to generate sequence of values.
even_number=[x for x in  range(1,11,1) if x%2==0 ]
# print(even_number)

square_number=[x**2 for x in  range(1,11,1) ]
# number=[x for x in  range(1,11,1) ]
# print(number)
correct_list=["apple","banana","grapes"]
in_list=["guaya","coconut","apple"]

op_list=[x for x in in_list if x in correct_list]

# print(op_list)

eid = [1, 2, 3, 4, 5]
ename = ["abhay", "parul", "jay", "priya", "mayank"]
address=["noida","delhi","patna","kerala","mumbai"]
columns=["eid","ename","address"]
employee_info = [{columns[0]: i, columns[1]: j, columns[2]: k} for i, j, k in zip(eid, ename, address)]
employee_dict = {"employee": employee_info}
# print(employee_dict["employee"][2]["ename"])
# print(employee_dict)



# function : you can create your own designed fucntion based on requirement
import datetime as dt

def validate_age(DOB, input_age, current_year):
    try:
        # Parse DOB string (assuming format like 'YYYY-MM-DD')
        dob = dt.datetime.strptime(DOB, '%Y-%m-%d')
        dob_year = dob.year
        
        # Calculate actual age
        today = dt.datetime.now()
        actual_age = current_year - dob_year
        
        # Adjust age if birthday hasn't occurred this year
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            actual_age -= 1
            
        # Compare input_age with calculated age
        return input_age == actual_age
    except ValueError:
        return False  # Return False for invalid date formats

# Example usage
# print(validate_age("1990-10-25", 35, 2025))  # True (if today is after Oct 25, 2025)
# print(validate_age("1990-11-01", 35, 2025))  # False (if today is before Nov 1, 2025)
# print(validate_age("invalid", 35, 2025))     # False (invalid date format)


# fucntion 2 salary_calculation
def calculate_salary(hours,payrate,currency):
    if currency=="dollar":
        payrate=payrate*85.2
        return float(hours*payrate)

employee={"eid":1,"hours":20,"payrate":20,"currency":"dollar"}
employee_salary=calculate_salary(employee["hours"],employee["payrate"]
                                 ,employee["currency"])
# print(f"the salary of the employee is : ",employee_salary)


# employee_salary=calculate_salary(employee["hours"],employee["payrate"])
# print(employee_salary)


eid = [1, 2, 3, 4, 5]
ename = ["abhay", "parul", "jay", "priya", "mayank"]
address=["noida","delhi","patna","kerala","mumbai"]
columns=["eid","ename","address"]
# employee_info = [{columns[0]: i, columns[1]: j, columns[2]: k} for i, j, k in zip(eid, ename, address)]


from utils1 import employee_information
employee_info=employee_information(columns,eid,ename,address)
employee_dict = {"employee": employee_info}
print(employee_dict)

'''
path=r'C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Notes\batch2\day3(202510251).txt'
with open(path,'w') as d:
    d.write(data)