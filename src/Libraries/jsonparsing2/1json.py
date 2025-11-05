
import json
import pandas as pd
path =r'C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Projects\Batch\src\Libraries\jsonparsing2\weather.json'
list_file=[]
with open(path,'r') as f:
    for i in f:
        if i:
            list_file.append(json.loads(i))

# print(len(list_file))
# print(list_file[:2])
# print(list_file[0].keys())
# df=pd.DataFrame(list_file)
# pd.set_option("display.max_rows", 1000)
# pd.set_option("display.max_columns", 1000)
# print(df.describe())
# # df=pd.DataFrame(list_file,columns=list_file[0].keys())

# with open("test1.csv",'w') as f:
#     f.write(str(list_file))

#  craete a dictionary so that a proper csv can be created
columns = list(list_file[0].keys())

# Create dict with empty lists for each column
final_dict = {col: [] for col in columns}
# print(final_dict)

for record in list_file:
    for col in columns:
        final_dict[col].append(record[col])
# number of rows
print(len(final_dict[columns[0]]))  # should be 366
#  number of columns
# print(final_dict.keys())
print(len(final_dict.values()))

del final_dict["WindGustDir"]

import csv

with open("test2.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=final_dict.keys())
    writer.writeheader()
    for row in zip(*final_dict.values()):
        writer.writerow(dict(zip(final_dict.keys(), row)))
