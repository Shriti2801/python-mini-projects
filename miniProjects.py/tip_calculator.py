print("WELCOME TO THE TIP CALCULATOR!")
print()
bill = float(input("What is the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = tip/100 * bill + bill
final_amount = round(bill_with_tip,2)
final_amount = "{:.2f}".format(bill_with_tip)
print("The bill per person is",final_amount)