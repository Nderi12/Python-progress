# Dictionary
# is an unordered set of key-value pairs, separated by comma and enclosed by curly braces.
# Vendor:Cisco, Model:2600, IOS:12.4, Ports:4

# create an empty dictionary
dict1 = {}

# add some data to our dictionary
dict1 = {"vendor":"Cisco", "model":"2600", "IOS": "12.4", "Ports":"4"}

# you can also use numbers for your dictionary keys
d1 = {1: "first element", 2: "second element"}

# Dictionary Methods
# output -> 12.4
print(dict1["IOS"])
print(dict1["vendor"])

# add a key-value pair
dict1["RAM"] = "128"

# modify the a key-valuepair in our dictionary
dict1["IOS"] = "15.6"

# deleting a pair in our dictionary -> using del command
del dict1["Ports"]

# find the number of key-value pairs -> using the len() function
print(len(dict1))

# verify if a certain string is or not a key in our dictionary
print("IOS" in dict1)
print("IOS2" in dict1)
print("IOS2" not in dict1)

# three important python function to deal with dictionaries
#1. the keys() method -> used to obtain
print(list(dict1.keys()))

# 2. values() method -> used to get a list conataining the values in a dictionary as elements
print(list(dict1.values())) 

# 3. items() -> 
# print(list(dict1.items())[2][1])
dict1_items = list(dict1.items())
print(dict1[2][1])

# print the dictionary
print(dict1)