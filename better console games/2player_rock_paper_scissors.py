import pwinput

#prompts player 1 to pick a name to use as a variable
player1 = str(input("Player 1, pick a name "))

#promps player 2 to pick a name to use as a variable
player2 = str(input("Player 2, pick a name "))


#this is how the users answers
move1 = pwinput.pwinput(prompt= str(player1 + str("'s move: ")), mask='*')

#covers up the screen so that noone can cheat
for i in range(9):
    print("   \n")

move2 = pwinput.pwinput(prompt= str(player2 + str("'s move: ")), mask='*')

#covers the screen
for o in range(9):
    print("   \n")


if str(move1) == str(move2):
    print(str(player1) + str(" and ") + str(player2) + str(" tied!"))
    
if move1 == str("Rock") and str(move2) == str("Scissors"):
    print(player1 + str(" picked Rock\n"))
    print(player2 + str(" picked Scissors\n"))
    print(player1 + str(" wins!"))
    
if move1 == str("Scissors") and str(move2) == str("Rock"):
    print(player1 + str(" picked Scissors\n"))
    print(player2 + str(" picked Rock\n"))
    print(player2 + str(" wins!"))
    
if move1 == str("Paper") and str(move2) == str("Rock"):
    print(player1 + str(" picked Paper\n"))
    print(player2 + str(" picked Rock\n"))
    print(player1 + str(" wins!"))
    
if move1 == str("Rock") and str(move2) == str("Paper"):
    print(player1 + " picked Rock\n")
    print(player2 + str(" picked Paper\n"))
    print(player2 + str(" wins!"))
    
if move1 == str("Scissors") and str(move2) == str("Paper"):
    print(player1 + str(" picked Scissors\n"))
    print(player2 + str(" picked Paper\n"))
    print(player1 + str(" wins!"))
    
if move1 == str("Paper") and str(move2) == str("Scissors"):
    print(player1 + str(" picked Paper\n"))
    print(player2 + str(" picked Scissors\n"))
    print(player2 + str(" wins!"))