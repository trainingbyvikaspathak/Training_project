import json

# some JSON String:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y)
print(y["age"])
