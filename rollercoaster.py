print("Welcome to Wonderla rollercoaster ride!!!")

#ask the user for their height and allow the user to ride only if their height is over 120cm
height = int(input("what is your height? "))

#initialise bill variable to give bill to the user
bill = 0
if height >= 120:
    print("You can ride")
    #ask the user for their age so that the bill can be given based on their age
    age = int(input("what is your age? "))
    if age <= 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    #if the user has midlife crisis
    elif age >= 45 and age <= 55:
        print("Free ride on us!")
    else:
        bill = 12
        print("Pay $12.")

    photo = input("Do you want a photo taken? Type y for yes and n for no!: ")

    if photo == "y":
        bill += 3
        print(f"Please pay ${bill}")
    else:
        print(f"Please pay {bill}")
else:
    print("you cannot ride the rollercoaster")
