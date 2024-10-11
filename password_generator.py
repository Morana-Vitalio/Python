import random

print("Welcome to the PyPassword Generator!")

# list of letters that include both lowercase and uppercase letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

nr_letters = int(input("How many letters would you like in your password?:\n"))
nr_symbols = int(input("How many symbols would you like in your password?:\n"))
nr_numbers = int(input("How many numbers would you like in your password?:\n"))

password_list = []

# Adding letters to the password
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Adding numbers to the password
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Adding symbols to the password
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Shuffling the generated characters
random.shuffle(password_list)

# Joining the list to form the final password
final_password = ''.join(password_list)
"""
 '' (empty string): This is the separator used between each element when joining them. 
 In this case, the empty string '' means that there will be no additional characters (like spaces or commas) 
 between the elements, so they will be joined directly next to each other.
 The join() method iterates over each element in password_list, 
 combining them into one continuous string without any separators.
For example, if password_list = ['a', 'B', '3', '%', 'y', 'Z', '9', '!'], 
using ''.join(password_list) will result in the string 'aB3%yZ9!'.

"""

print(f"Your generated password is: {final_password}")
