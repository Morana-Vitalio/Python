#Band name generator
"""
Ask the name of the city that the user lived in and the users pet name
concatenate these two to generate a band name
"""
#print welcome statement welcoming the user to the band name generator
print("Welcome to the Band name generator")
#asking for users city and pet name
city = input("What city did you grow up in?\n")
pet = input("Enter the name of your pet\n")
#generating band name by combining city and pet name
band_name = print("Your band name is:" , city.upper(), pet.upper())