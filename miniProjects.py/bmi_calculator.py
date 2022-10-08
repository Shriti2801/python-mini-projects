print("BMI CALCULATOR")
print()
weight = input("What is your weight in kg?\n")
height = input("What is your height in m?\n")
bmi = int(weight)/float(height)**2
int_bmi = int(bmi)
print("Your BMI is",int_bmi)
