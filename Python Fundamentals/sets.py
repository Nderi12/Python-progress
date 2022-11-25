# sets
# a set is basically an unordered collection of unique elements.
# you may regard sets as lists that have no duplicates
# ways of creating a set
# 1. set() function
list1 = [1, 2, 3, 4, 5, 2, 3]
print(list1)
print(set(list1))

# creating a set directly by passing a raw sequence to the set()
set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
print(set1)
print(type(set1))

# 2. using curly braces
set2 = {11, 12, 13, 14, 15, 15, 15, 11}

# finding the length of a set
print(len(set2))

# check for membership using 'in' and 'not in' keywords
print(11 in set2)
print(10 in set2)
print(10 not in set2)

# adding an item/element to a set - using the add() method
set2.add(16)
set2.add(20)

# removing an element form a set uding remove() method
set2.remove(11)

# sets don't allow duplicate
set2.add(16)
set2.add(20)

# print(set2)

# set methods and operations
set3 = {1, 2, 3, 4}
set4 = {3, 5, 8}

# identify the common elements in the two sets - using intersection() method
print(set3.intersection(set4))
print(set4.intersection(set3))

# identify the differnce between two sets - using difference() method
print(set3.difference(set4))
print(set4.difference(set3))

# unifying sets - using the union() method
print(set3.union(set4))

# remove a random element in a set - using pop() method
set3.pop()

# we can clear a set - using clear() method
set3.clear()

# set3 = {}

print(set3, type(set3))



