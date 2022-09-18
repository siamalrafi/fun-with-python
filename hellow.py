# check negative or positive number

""" number = input('Please input your number - ')
number = int(number)

if number < 0:
    print('It is a negative number')
else:
    print('It is a positive number') """


# check odd or even number

""" number = input('Please input your number - ')
number = int(number)

if (number % 2) == 0:
    print('It is a even number')
else:
    print('It is a odd number') """


# find the largest number from a list

""" heights = [0, 2, 300, 10, 11, 1000]

largest_number = heights[0]

for number in heights:
    if number > largest_number:
        largest_number = number

print(largest_number)
 """


# Find the large number using function

""" def numebrlist(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        print("I'm big ", number1)
    elif number2 > number1 and number2 > number3:
        print("I'm big ", number2)
    else:
        print("I'm big ", number3)

numebrlist(10, 222, 30) """


# Find the leap year using function

""" 
def IsLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, ' is a leap year')
    else:
        print(year, ' is not a leap year')


IsLeap(2222) """
""" 
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('yes')
            else:
                print('no')
        else:
            print('yes')
    else:
        print('no')


isLeapYear(2002) """
""" 
year = int(input('Enter year : '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
 """


# turtle example

""" import turtle

turtle.forward(1000)

turtle.exitonclick() """
