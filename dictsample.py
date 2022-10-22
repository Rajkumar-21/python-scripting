mydict={}
print(type(mydict))
dict1={
    "name":"Rajkumar",
    "age":25,
    "location": "Palakkad"
}

print(dict1['name']) # using keys
print(dict1.get("age")) # using get method
print(dict1.keys()) # list all keys only in the dict
print(dict1.values()) # listing only values from the dict
print(dict1.__len__()) # getting total dicts 
print(dir(dict1)) # get the available methods in the type of dict object
removed_item=dict1.popitem() # removing the key:value object from the dict
print(removed_item)
new_dict={
    "Passedout":2019,
    "College": "REC"
}
dict1.update(new_dict) # updating/adding other dict to this
print(dict1)

#fromkeys method

keys= {'a','e','i','o','u'}
newdict1=dict.fromkeys(keys)
print(newdict1)
newdict1['a']="first letter"
print(newdict1)