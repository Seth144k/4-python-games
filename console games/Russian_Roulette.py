import random

#this determines the spin of the gun
spin = random.randint(1, 6)

#this is where the user makes an integer input to determine where the bullet is loaded
bullet = int(input("Load the six-shooter with a number between 1 and 6: "))

print("You load the bullet\n")

print("You spin the chamber as fast as you could hoping to live another day")

print("You think over your life choices as it's spinning")

print("You raise the gun to your head\n")

#this is where the user number matches where the spinner lands on to deetermine if your dead
spinner = random.randint(1, 6)

#the spinner and number matches up
if spinner == spin:
    print("The gun goes off. You are dead")
    
#if the numbers dont match
if spinner != spin:
    print("The gun makes a clicking noise rendering you unharmed. You live to see another day")