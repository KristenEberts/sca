import random
import cs50

number = random.randint(1,100)

guess = cs50.get_int("I'm thinking of a number between 1 and 100... What is it? ")

if guess == number:
    print("Nice job! You win!")
elif guess > number:
    print("Too high! Guess lower!")
else:
    print("Too low! Guess higher!")
    
