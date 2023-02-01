# exercise for finding out how old someone will be in 100 years via user input:
"""
age = int(input("How old are you? "))
name = input("What's your name? ")
toBeHundred = 100 - age
print(f"{name} you are going to be 100 years old after {toBeHundred} years!")

# Odds or Evens on input
userNum = int(input("Please enter a number: "))
def oddOrEven(number):
    if number %2 == 0 and number %4 != 0:
        print(f"The number you selected, {number}, is even")
    elif number % 2 == 0 and number % 4 == 0:
        print(f"The number you selected, {number}, is both even and divisible by 4")
    elif number %2 !=0:
        print(f"The number that you have selected, {number}, is odd.")
    else:
        print("Please enter a number")     

oddOrEven(userNum)
# Odds or Evens from an array of numbers
numbers = [12, 3, 5, 60, 78, 42, 57, 94, 343, 87, 9]
def listofnums(nums):
    new_list = []
    for num in nums:
        if num %2 != 0:
            new_list.append(num)
    return new_list        

result = listofnums(numbers)
print(result)
"""

# List less than Ten
# Remove the Elif if you just want the string of numbers less than ten, but this is an example of differentiating.

numberstoten = [1, 2, 435, 7, 3, 56, 78, 32, 0, 8]

def lessThanTen(numberstoten):
    for num in numberstoten:
        if num < 10:
            print(num)
        elif num >= 10:
            print("This number is greater than 10")
        else: 
            print("please enter a number")    

lessThanTen(numberstoten)            


# Divisors, enter a number and print out list of all divisors of that number:
# Easy way to create a list of numbers 2 to 10 is x= range(2, 11)

num = int(input("Tell me a number "))

c = range(1, (num + 1))

for count in c:
    if num % count == 0:
        print(count)

