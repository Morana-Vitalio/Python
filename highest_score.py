#replicate the max() function using lists, loops and conditionals concept.
#max function allows you to pass a list of numbers and picks out the largest value from the list
print("Max Value")
numbers = [10,20,30,40,50,60,70,80,90,100,120]

max_num = 0
for number in numbers:
    if number > max_num:
        max_num = number
        
print(max_num) 

#The Gauss challenge
#Add all the numbers from 1 to 100
sum = 0
for number in range(1, 101):
    sum += number
    
print(sum)