# most of the data in general practice are semi structuired
# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y=json.loads(x)
# print(type(y))
# import json

# path = r'C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Projects\Batch\src\Libraries\titanic.json'
# # Open the file before loading
# with open(path, 'r') as f:
#     data = json.load(f)

# print(type(data))  # usually <class 'dict'> or <class 'list'>

# import json
# x =  '[1,2,3,4,5,6,7,8,9,10]'
# y=json.loads(x)
# print(type(y))
# print(y)

# import json
# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# print(json.dumps("\"foo\bar"))
# print(json.dumps('\u1234'))
# print(json.dumps('\\'))
# print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))


# import json
# print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ': ')))
# print(json.dumps([1, 2, 3, {'4': 5, '6': 7}]))


import json

# Step 1: Take input string (like a dictionary)"
input_str = '{"name": "Ravi", "age": 27, "city": "Pune","lang":"Hindi","hobby":"chess"}'

# Step 2: Convert string to Python dictionary
data_dict = json.loads(input_str)
# print formatted JSON string
print(json.dumps(data_dict, indent=4))
