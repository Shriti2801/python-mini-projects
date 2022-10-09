import random
print("Lets play Rock, Paper, Scissors!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors:\n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid number. Your Lose!")
else:
    print(game_img[user_choice])

    comp_choice = random.randint(0,2)
    print("The computer choses:",comp_choice)
    print(game_img[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("You Win!")
    elif user_choice == 2 and comp_choice == 0:
        print("You Lose!")
    elif comp_choice > user_choice:
        print("You Lose!")
    elif user_choice > comp_choice:
        print("You Win!")
    elif comp_choice == user_choice:
        print("It's a draw.")

