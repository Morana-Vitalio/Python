"""
create a program that either prints out, "Heads", or it prints out "Tails", and whether

if it prints out Heads or Tails will entirely depend on a random number that you generate.
"""
import random

print("Welcome to Heads or Tails game")

#pass a list to generate a rando choice of heads or tails
coin_choice = random.choice(["Heads", "Tails"])

#Generating random numbers between 1 and 10
number = random.randint(0, 1)

print(f"The choice is {coin_choice} and the number is {number}")


#else generating random choices as 0 for heads and 1 for tails
if number == 0:
    print("Heads")
else:
    print("Tails")