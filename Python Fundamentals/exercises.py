# # write a python program that asks the user for their age and print it out in seconds
# user_name = input("Please enter your name: ")
# user_age = int(input("Please enter Your Age: "))

# age_in_seconds = user_age * 365 * 24 * 60 * 60

# print("Hello, " + user_name + " You have lived for " + str(age_in_seconds) + " seconds")
# print(f"Hello {user_name}, You have lived for {age_in_seconds} seconds")
# print("Hello {}, You have lived for {} seconds.".format(user_name, age_in_seconds))

# get the scores of each subject from the user
math = int(input("Enter score for math: "))
kisw = int(input("Enter score for kisw: "))
eng = int(input("Enter score for eng: "))
chem = int(input("Enter score for chem: "))
sst = int(input("Enter score for sst: "))

# store them in a list
scores = [math, kisw, eng, chem, sst]
# create an empty list
scores = []
scores.append(math)
scores.append(kisw)
scores.append(eng)
scores.append(chem)
scores.append(sst)

# calculate the average score
average_score = sum(scores) / len(scores)

# display the average score to the user
print(f"The average score is: {average_score}")

# 26/09/2022

# create a list that generates and prints a list of numbers from 1 to 20. please do not create the list manually
li = list(range(1, 21))
print(li)

# complete the script so that it removes the duplicate elements in the list
a = ["1", 1, 2, "2", "2", "1", 3, 1]
a = set(a)
print(a)
print(set(a))