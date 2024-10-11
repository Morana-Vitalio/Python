"""
create a rock paper scissor game. Allow the user to choose a number for rock(0), paper(1), scissor(2).
let the computer generate a random choice for itself and declare winner based on rules
"""
import random

print("Welcome to rock, paper and scissor game!!")
user_choice = int(input("Please choose 0 for rock, 1 for paper and 2 for scissor!: "))

if user_choice > 2 or user_choice < 0:
    print("Invalid choice, please try again!")
 
options = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",

"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

print("You chose: ")
print(options[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(options[computer_choice])

if user_choice == computer_choice:
    print("Draw!!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")




