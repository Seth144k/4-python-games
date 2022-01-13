import math
import random

#makes a random number genorator between 1 and 5
num = random.randint(1, 5)

#user input for guessing
guess = input("Guess a number between 1 and 5: ")

#this activates when the guess IS equal to the random number
if guess == str(num):
    print("You win!")
#this activates when the guess is NOT equal to the random number
if guess != str(num):
    print("You lose!\n")
    print("The number was: " + str(num))