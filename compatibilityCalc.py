print("This is a compatibility calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
str_lower_case = combined_string.lower()
t = str_lower_case.count("t")
r = str_lower_case.count("r")
u = str_lower_case.count("u")
e = str_lower_case.count("e")

true = t + r + u + e

l = str_lower_case.count("l")
o = str_lower_case.count("o")
v = str_lower_case.count("v")
e = str_lower_case.count("e")

love = l + o + v + e
compatiblity_score = int(str(true) + str(love))

if (compatiblity_score < 10) or (compatiblity_score > 90):
    print(f"Your score is {compatiblity_score}, you go together like coke and mentos.")
elif (compatiblity_score >= 40) and (compatiblity_score <= 50):
    print(f"Your score is {compatiblity_score}, you are alright together.")
else:
    print(f"Your score is {compatiblity_score}.")
