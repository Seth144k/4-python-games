import random
import playsound

playsound.playsound("diceRoll.mp3")

print("Your dice number is: " + str(random.randrange(1, 6)))
