# Python dictionary
'''
Dictionary are the ordered collection of data items or value key pair.
they store multiple items in a single variable.
dictionary items are the key value pair separated by commas end enclosed by curly braces

'''
info = {
    "name":"Abhishek Verma",
    "age":21,
    "eligible":True
}
print(info)


# print(info["name2"]) #if name2 value is not present in info then it will send an error
print(info.get("name2")) #if not present send an none message not error

# it will print info dictionary
print(info.items())
# info,keys() is a list of all the keys 
print(info.keys())
# info.values() is a list of all the values
print(info.values())

print()
for keys in info.keys():
    # it will give all the value
    # keys wiil give you only keys
    print(keys,info[keys])

for key,value in info.items():
    print(f"the value corresponding to the key {key} is: {value}")