print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure!")
choice1 = input('You are at a crossroad. Where do you want to go? Type "Left" or "Right".\n').lower()
if choice1 == "left":
    choice2 = input('You have come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('You have arrived at a castle. The entrace has three doors, one red, one yellow, one blue. Which one do you choose?\n').lower()
        if choice3 == "red":
            print("Ooops! This is a room full of fire. Game Over")
        elif choice3 == "blue":
            print("You have entered a room full of beasts. Game Over")
        elif choice3 == "yellow":
            print("Hurray! You have found the treasure.\nYou Win")
        else:
            print("This door does not exist. Game Over")
    else:
        print("Yumm! The crocodiles had a great dinner. Game Over")
else:
    print("Ouch! You fell of the road! Game Over!")
