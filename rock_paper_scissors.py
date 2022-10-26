import random

#the choices that the AI could pick
choices = ["Rock", "Paper", "Scissors"]

#how the opponent picks a choice
action = random.choice(choices)

#this is how the user answers
makemove = input("Rock, Paper, or Scissors? ")

if makemove == str("Rock") and action == str("Scissors"):
    print("Your opponent picked Scissors\n")
    print("You picked Rock\n")
    print("You win!")
    
if makemove == str("Scissors") and action == str("Rock"):
    print("Your opponent picked Rock\n")
    print("You picked Scissors\n")
    print("You lose!")
    
if makemove == str("Paper") and action == str("Rock"):
    print("Your opponent picked Rock\n")
    print("You picked paper\n")
    print("You win!")
    
if makemove == str("Rock") and action == str("Paper"):
    print("Your opponent picked Paper\n")
    print("You picked Rock\n")
    print("You lose!")
    
if makemove == str("Scissors") and action == str("Paper"):
    print("Your oppenent picked Paper\n")
    print("You picked Scissors\n")
    print("You win!")
    
if makemove == str("Paper") and action == str("Scissors"):
    print("Your opponent picked Scissors\n")
    print("You picked Paper\n")    
    print("You lose!")