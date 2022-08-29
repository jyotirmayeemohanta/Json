import json
d={"4": 5,"6": 7,"1": 3,"2": 4}
print(d)
print("\nJSON data:")
print(json.dumps(d,sort_keys=True,indent=4))




# a=json.loads(d)
# print(a)



{
    "1": 3,
    "2": 4,
    "4": 5,
    "6": 7
}