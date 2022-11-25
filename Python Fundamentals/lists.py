# creating our first empty list
list1 = []
print(list1)

# populate or add elements to our empty
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

# print(type(list1))
print(list1)

# find the len of the list - using len()
print(len(list1))

# accessing the first element of the list
print(list1[0])

# access the last element of the list
print(list1[-1])

# return IndexError -> if you enter an invalid index
# print(list1[100])

# list1[2] = "HP"
print(list1)

list2 = [-11, 2, 12]
# finding the smallest/minimum number -> min()
print(min(list2))

# finding the largest/maximu number -> max()
print(max(list2))

list3 = ["a", "b", "c"]
print(min(list3))
print(max(list3))

# print(min(list1))
# print(max(list1))

# Adding elements to a list -> using append() method
list1.append(100)
list1.append("HP")

# Removing an element from a list
# 1. using del keyword
del list1[6]
del list1[6]
print(list1)

# 2 removing an element from a list using its index
list1.pop(0)
print(list1)

# 3. removing an element by specifying the element itself
list1.remove("Avaya")
print(list1)

# inserting an element at a specific index -> using insert()
list1.insert(2, "Nortel")
print(list1)

# appending a list to another list
list4 = [9, 99, 999]

list1.extend(list4)
print(list1)

# finding the index of an element inside of a list
print(list1.index(10.5))
print(list1.index(99))

# adding element 10 twice
list1.append(10)
list1.append(10)
print(f"Element 10 0ccurs {list1.count(10)} times.")

# sorting list elements in ascending order -> using sort() method
list2.append(1)
list2.append(25)
list2.sort()
print(list2)

# sorting a list in a descending order
list2.reverse()
print(list2)

# sorting a list using the sorted() method
list4.append(1)
list4.append(25)
list4.append(500)
print(sorted(list4))

# sorting a list using sorted() in a reverse order
print(sorted(list4, reverse=True))

# concatenate or repeat a list using plus and multiplication operators
# adds the elements of both lists together -> plus (+)
print(list1 + list4)

# repeats list2 as many times as you want, in this case, 3 times
print(list2 * 3)

# lists slices
# var1[5 : 10]
list5 = [1, 2, 3, 'a', 'b', 'c']
# extracting the first three elements -> [1, 2, 3]
print(list5[0:3])
print(list5[:3])
# output [3, 'a', 'b']
print(list5[2:5])
print(list5[2:-1])

# [3, 'a', 'b', 'c']
print(list5[2:])
# extract the entire list
print(list5[:])

# using negative indexes
print(list5[-4:-1])

# extract the last three elements using negative indexes
print(list5[-3:])

# all the elements minus the last three elements
print(list5[:-3])

# using a step -> [1, 3, 'b]
print(list5[::2])

# reversing a list using a step -> ['c', 'b', 'a', 3, 2, 1]
print(list5[::-1])