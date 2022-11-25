r = list(range(10))
print(r)

# indexing
# get the first element
print(r[0])
# get the last element
print(r[-1])

# check if a certain element is a member of the range
print(10 not in r)
print(7 in r)

# getting the index of an element in a range - index()
print(r.index(5))

# slicing ranges
r = range(10)
print(list(r)[2:5])

# next class -> Dictionries
user_age = int(input("Enter your age: "))
decades_lived = user_age // 10
print(f"You have lived for {decades_lived} decades.")