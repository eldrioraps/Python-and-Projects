# """
# Understand how variables work in Python
# Identify and use basic data types
# Perform operations using arithmetic and logical operators
# Write small programs combining user input and calculations
# """


# variable 
# datat types int,float,str,list,bool,tuple,set,dict
#  a list variable is used to contain more then one value comma seprated in the square brackets
#  there are multiple operation one can perform in a list
#  
a=1
b=1.1
c="python"
d=True   
e=[1,2,3]
f=(1,2,3,4,4)
g={1,2,2,3,3,4,4}
h={"ename":"venkatesh"}
# print(type(h))
# print(h)

# list --append any value, remove any value,get range of values,copy a list,isnert a value
names=["abhay","payal","rahul","jay","priyanka"]
# print(names)
# names.append("priya")
# print(names[0])
# print(names[:2])
# names.remove("abhay")
# names.remove(names[2])
names[2]="mayank"
names.insert(2,"rahul")
names2=names.copy() 
names3=names
# print(names)
# print(names2)
# print(names3)

#  dict: it is combination of key value pairs, then json can b easily converted to dict or vice verssa
# employee_info={
#     "ename":"abhay",
#     "age":25,
#     "gender":"male",
#     "address":"noida"
# }

#  "abhay" 25,"male" "noida" ["chess","badminton","cricket","football","music"]
ename="abhay"
age= 25
gender="male"
address="noida"
hobbies=["chess","badminton","cricket","football","music"]
# ename=input("enter you name: ")
# age= input ("enter your age: ")
# gender=input ("enter gender: ")
# address=input("enter address: ")
# hobbies=input("enter hobbies comma sepearted: ")

employee_info={"employees":[{
    "employee_code":101,
    "ename":ename,
    "age":age,
    "gender":gender,
    "address":address,
    "hobbies":hobbies,
    "project_details": [{"projectname":"sql development for LLM",
                         "designation":"SQL developer",
                         "salary": "15 LPA",
                         "duration":"5 months"},
                         {"projectname":"SSIS development data migration",
                         "designation":"SSIS developer",
                         "salary": "22 LPA",
                         "duration":"15 months"}
                         
                         ]
    
},
{
    "employee_code":102,
    "ename":"priya",
    "age":28,
    "gender":"Female",
    "address":"delhi",
    "hobbies":["chess","badminton"],
    "project_details": [{"projectname":"sql development for LLM",
                         "designation":"SQL developer",
                         "salary": "15 LPA",
                         "duration":"5 months"},
                         {"projectname":"SSIS development data migration",
                         "designation":"SSIS developer",
                         "salary": "22 LPA",
                         "duration":"15 months"}
                         
                         ]
    
}
]
}

# print(employee_info)
# print(employee_info.keys())
# print(employee_info.values())
# print(employee_info["hobbies"][2])
# print(employee_info["employees"][1]["project_details"][1]["projectname"])

# mathematical operator + - % / // **
print(2**3)
print(2*3)
print(1+2)
print(5%2)
print(5/2)
print(5//2)

# logical operator and or not 