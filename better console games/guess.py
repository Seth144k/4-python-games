import sys
import random

round = int(input("How many attempts would you like? "))
guesser = int(random.randint(0, 5))

if round <= 0:
    print("round cannot go equal to or less than 0")
    sys.exit()

if round > 0:
    while round > 0:
        guess = int(input("Guess any number between 0 and 5 ").strip())

        round = round - 1

        print("You have " + str(round) + " attempt(s) left")

        if guess == guesser and round > 0:
            print("You win!")
            sys.exit()
        elif guess != guesser and round <= 0:
            print("You lose!\n")
            print("The number was " + str(guesser))
            sys.exit()

    if round <= 0:
        print("no more attempts")
