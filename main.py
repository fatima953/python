import math
a = float(input("enter a decimal number:"))
print("ceil:", math.ceil(a))
print("floor:", math.floor(a))
print("Welcome to guess the number game")
print("i will guess a number, you need to guess my number between 1 and 100")
import random 
ran_choise =  random.randint(1,100)
while True:
    try:
     num = int(input("enter the number"))
     if num == ran_choise:
        print("yes, you got the number")
        break
     elif num < ran_choise:
        print("the number is bigger then your guess")
     elif num > ran_choise:
        print("the number is smaller then your then your guess")
    except ValueError as er:
        print("invalid input")
    
print("thank you for playing")