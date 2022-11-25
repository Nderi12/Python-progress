my_string = "this is my first string"
# print(type(my_string))
# print(my_string)

my_string2 = """This
is\n
my\n
second\n
string"""
# print(my_string2)

# \n -> New line character for inserting new lines

string1 = "Cisco Router"
print(string1[0])
print(string1[5])
print(string1[-1])


# len() -> returns the number of items in a sequence
print(len(string1))

print(string1[11])
# print(string1[20])

# python strings methods
# index() method

a = "Cisco Switch"
print(a[1]) # indexing
print(a.index("i"))

# count the occurences of element "i"
print(a.count("S"))

# find()
print(a.find("sco"))

# lower() and upper()
print(a.lower())

print(a.upper())
print(a)

# startswith() and endswith()
print(a.startswith("C"))
print(a.startswith("Cis"))

print(a.endswith("q"))
print(a.endswith("tch"))

# strip(), split() and join()
b = "   Cisco Switch    "
print(b)
print(b.strip())

c = "$$$cisco switch$$$"
print(a.strip("$"))

# replace() method
print(b.replace("c", "*"))

d = "Cisco,Juniper,Hp,Avaya,Nortel"
print(d.split(","))

# c_i_s_c_o__s_w_i_t_c_h
# "_"
print("#".join(a))

# Strings Slices (Slicing)
