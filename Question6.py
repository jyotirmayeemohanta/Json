import json
j='{"a":1, "a":2, "a":3, "a":4, "b":1, "b":2}'
print("Original python object:")
print(j)
a=json.loads(j)
print("\nUnique key in a JSON object:")
print(a)



