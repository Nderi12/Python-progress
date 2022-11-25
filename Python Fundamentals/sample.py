fruits_list = ["apples", "berries"]

# find the length of the list
print(len(fruits_list))

# indexes
print(fruits_list[-1])

# modify an element inside a list
fruits_list[1] = "cherries"

# append/add an item into the list
fruits_list.append("dates")
# fruits_list.append("bananas")

# insert into position
fruits_list.insert(0, "bananas")

# copy a list
new_fruits_list = fruits_list.copy()

# # remove an item from a list
# del fruits_list[0]
# fruits_list.pop(0)
# fruits_list.remove("dates")

# clear a list
new_fruits_list.clear()

# adding to a list
added_fruits_list = fruits_list + new_fruits_list

# repeat a list(s)
# print(new_fruits_list * 5)

# list slicing
print(fruits_list[1:3])

# sorting a list
fruits_list.sort()

print(fruits_list) 
# print(new_fruits_list)
# print(added_fruits_list)

# return index of an item
print(fruits_list.index("dates"))