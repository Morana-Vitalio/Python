"""
develop a python program for pizza delivery
first welcome the user to the pizza delivery program
ask the size of the pizza they want s,m or l
ask if they want pepperoni
ask if they want extra cheese
print a final bill depending on their choices
"""
print("Welcome to pizza delivery program!!")
#ask the pizza size that user wants
size = input("what size pizza do you want? S, M, L?: ")
#ask if the user wants pepperoni
pepperoni = input("Do you want pepperoni? y for yes and n for no: ")
#ask if the user wants extra cheese.
extra_cheese = input("Do you want extra cheese? y for yes and n for no: ")


#initialise bill variable to calculate bill
bill = 0


if size == "S":
    bill = 10
elif size == "M":
    bill = 15
elif size == "L":
    bill = 20
else:
    print("Please choose valid size!")

#if yes for pepperoni then add $5 to their total bill
if pepperoni == "y":
    bill += 5
    
#If yes for extra cheese then add $5 to their total bill
if extra_cheese == "y":
    bill += 5

print(f"Your final bill is ${bill}")