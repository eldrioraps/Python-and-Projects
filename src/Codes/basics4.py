data="""
# map(),reduce(),filter(),lambda 
# map() function in Python applies a given function to each element of an iterable (list, tuple, set, etc.) and returns a map object (iterator). It is a higher-order function used for uniform element-wise transformations, enabling concise and efficient code.
# Lambda Functions are anonymous functions means that the function is without a name. 
# filter():Applies a function that returns True or False to each item in an iterable, and returns a new iterable with only the items where the function returns True.
# Reduce(): Applies a function cumulatively to the items of an iterable, reducing it to a single value (e.g., sum, product).
#  split()
# sorted(): sort the list
a=["ind","us","aus","nz"]
# for i in a:
#     # i==i.upper()
#     print(i.upper())

b=map(lambda x:x.upper(),a)
a=list(b).copy()
# print(list(a))

country=["ind","us","aus","nz"]
# country_filter = filter(lambda x: x == "us" or x=="ind", country)
country_filter = filter(lambda x: x in ["us","ind"], country)
# print(list(country_filter))


from functools import reduce
a = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, a, 100)  # start with 0 as initial value
# print(total)

from functools import reduce
a = [1, 2, 3, 4, 5] 
total = reduce(lambda acc, x: acc + x**2, a, 0)  # start with 0 as initial value
# print(total)

from functools import reduce
logs = [
    "INFO: User logged in",
    "ERROR: Database timeout",
    "INFO: Request processed",
    "ERROR: Authentication failed",
    "ERROR: Database timeout"
]
log_defination=map(lambda x: x.split(": ",1)[0],logs)
log_detail=map(lambda x: x.split(": ",1)[1],logs)
# print(list(log_defination))
# print(list(log_detail))


address=["123 street sector42 noida UP India"]
address_component=(lambda x:x.split(" ",10))
# print(address_component(address[0]))

from functools import reduce
speech="APJ Abdul Kalam's speeches are known for their inspirational messages on dreaming big, working hard, and developing a strong sense of self-belief. He encouraged individuals to overcome challenges through persistence and to contribute to national development with a focus on innovation and self-reliance. His speeches often called for a greater emphasis on education, values, and developing a vision for the future, making them a source of motivation for students and leaders alike.  "
speech_words=(lambda x: x.split(" ",100000))
words=speech_words(speech)
word_count=reduce((lambda acc,x:{**acc,x:acc.get(x,0)+1}),words,{})
print(word_count)
# print(word_count)


# x:acc.get(x,0)+1
# x=keys
# acc.get(x,0)+1=value of a dict

# diction={"ename":"ravi"}
# print(diction.get("eid",0))



# print(type(words))
# print(len(speech_words(speech)))




a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x**2, a))
# print(b)

a = {"eid": 1, "ename": "priya"}
keys = a.keys()
values = map(lambda x: str(x).upper(), a.values())
a = dict(zip(keys, values))
# print(a)


#  sorting of numbers
#  use sorted(iterable,key=expression)
a=list(x for x in range(100))
sort_number=sorted(a,key=lambda x:x in a)
a=[-100,-120,5,4,58,20,56]
sorted_number=sorted(a,key=lambda x : x**3)

a=[-100,-120,5,4,58,20,56]
sorted_number=sorted(a,key=lambda x : x%10)
val=lambda x: x%10
# print(list(map(val,a)))
# print(sorted_number)
from functools import reduce
logs = [
    "INFO: User logged in",
    "ERROR: Database timeout",
    "INFO: Request processed",
    "ERROR: Authentication failed",
    "ERROR: Database timeout"
]
errors = filter(lambda log: "ERROR" in log, logs)
error_types=map(lambda types: types.split(": ")[1],errors)
error_count=reduce(lambda acc, err:{**acc, err:acc.get(err,0)+1},error_types,{})
# error_counts = reduce(lambda acc, err: {**acc, err: acc.get(err, 0) + 1}, error_types, {})
# print(error_count)

"""

path=r'C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Notes\batch2\day3Part2(20251025).txt'
with open(path,'w') as c:
    content=c.write(data)
