# Tuples
my_tuple = (1, 2, 3, 4, 5)
# my_tuple2 = (9,)
# print(type(my_tuple2))

# indexing
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[4])

# modifying an element of my_tuple -> impossible
# my_tuple[1] = 10

# removing an element from a tuple
# del my_tuple[0]

# print(type(my_tuple))

# tuple assignment
tuple1 = ("Cisco", "2600", "12.4")
# assign a tuple of variables to tuple1
(vendor, model, ios) = tuple1
# check if variable-to-value mapping has been properly performed
print(vendor)
print(model)
print(ios)

tuple2 = (1, 2, 3, 4) # (4, 3, 2, 1)
# (x, y, z) = tuple2
# print(x)


# Tuple Methods
# find the number of elements in a tuple -> using len()
print(len(tuple2))

# finding the lowest and greatest element inside a tuple -> using min() and max()
print(min(tuple2))
print(max(tuple2))

# conacate a tuple -> using + operator
print(tuple2 + (5, 6, 7, 8))

# repeating a tuple -> using * operator
print(tuple2 * 3)

# slicing
print(tuple2[:2]) #  (1, 2)
print(tuple2[1:3])
print(tuple2[2:])
print(tuple2[-2:])

# reversing a tuple using slicing and a step
# variable[start:stop:step]
print(tuple2[::-1])

# skip the second element of a tuple
print(tuple2[::2])

# check for membership
print(5 in tuple2) # False
print(10 not in tuple2) # True

# deleting a tuple entirely
del tuple2
print(tuple2)




