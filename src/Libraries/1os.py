# os :this allow you to create or manipulate files in the system.
import os
path=r'C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Projects\Batch\src\Libraries\1os.py'
print(os.getcwd())
print(os.listdir())
if os.path.exists(path)==True:
    print('do further logic')
else:
    print('Please check the file do not exists')

print(os.path.exists(path))