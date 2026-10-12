# Dictionary - Collection of key : value pairs. Unordered, mutable, fast.
# 3 Main Rules:
# Key:Value - {"key": value}
# Keys must be UNIQUE & IMMUTABLE - No duplicate keys, key can't be a list
# Values can be anything - Duplicate allowed, mutable allowed

my_dict = {"name": "Debojyoti", 
           "age": 25, 
           "is_student": True, 
           "hobbies": ["coding", "reading", "gaming"]}

data = {0:65, 1: "Debojyoti", 2: True, 3: [1, 2, 3], 4: {"name": "Debojyoti", "age": 25}}
print(data[1])

# data = {"Debojyoti": 33, "Sandipan": 59, "Anuska": 48, "Sneha": 24}
# print(data[33]) # This will raise a KeyError since 33 is not a key in the dictionary
#print(data["Debojyoti"])
print(data.get("Sandipan")) # This will return the value associated with the key "Sandipan" (59)
print(data.get(1)) # This will return None since 1 is not a key in the dictionary
print(data.get("Anuska", "Key not found")) # This will return the value associated with the key "Anuska" (48)

print(my_dict.get("is_student")) # This will return True, the value associated with the key "is_student"

print(my_dict.keys()) # This will return a view object containing the keys of the dictionary
print(my_dict.values()) # This will return a view object containing the values of the dictionary
print(my_dict.items()) # This will return a view object containing the key-value pairs of the dictionary

print("\n\n\n\n\n\n\n\n")

print(data.get("Anushka", "Key not found")) # This will return "Key not found" since "Anushka" is not a key in the dictionary

print(data.pop(2)) # This will remove the key-value pair with the key "Debojyoti" from the dictionary
del data[3] # This will remove the key-value pair with the key 3 from the dictionary
print(data) # This will print the updated dictionary after removing the key-value pairs

data.update({"new_key": "new_value"}) # This will add a new key-value pair to the dictionary
print(data) # This will print the updated dictionary after adding the new key-value pair
data.update({"name": "Anuska"}) # This will update the value associated with the key "name" in the dictionary
print(data) # This will print the updated dictionary after updating the value associated with the key "name"

# Another way to create a dictionary is by using the dict() constructor. 
# For example:
new_dict = dict(name="Debojyoti", age=25, is_student=True)
print(new_dict)

# nested dictionaries are also possible. For example:
# Method 1: Direct nested with dict()
nested_dict_1 = dict(
    id = 65,
    info = dict(name="Debojyoti", age=25),
    marks = dict(obtained=73, total=137),
    extra = dict(active=True, scores=[1,2,3])
)

print(nested_dict_1)

# Method 2: Direct nested with {}
data = dict({
    0: 65,
    1: "Debojyoti",
    2: True,
    3: [1, 2, 3],
    4: dict(name="Debojyoti", age=25) # <-- nested dict here
})

print(data[4]["name"]) # Debojyoti
print(data[4]["age"]) # 25

students = dict(
    debojyoti = dict(age=25, obtained=73, total=137),
    rahul = dict(age=22, obtained=80, total=137)
)

print(students["debojyoti"]["obtained"]) # 73
print(students["rahul"]["obtained"]) # 80
print(students["debojyoti"]["age"]) # 25
print("\n\n\n\n\n\n\n\n")

# Practice problem from Telusko
Princey = {
    "harsh" : ["java","python","AI"],
    "navin" : {'Frontend': "React",'Backend':"Spring"},
    "Kiran" : ["js","Flask"]               
}

print(Princey["navin"]["Backend"])