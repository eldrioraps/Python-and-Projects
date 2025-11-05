import json
import pandas as pd

path=r'C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Projects\Batch\src\Libraries\jsonparsing2\weather.json'
with open(path,'r') as f:
    list_json=[]
    for i in f:
        if i:
            list_json.append(json.loads(i))

print(len(list_json))
# print(json.dumps(list_json[1],indent=4))
final_dict={}
for index,item in enumerate(list_json):
    final_dict[index]=item

# print((final_dict[0]))

df = pd.DataFrame.from_dict(final_dict, orient='index')
print(df.head())