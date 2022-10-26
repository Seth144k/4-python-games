import time
import sys

num = int(input("Countdown from when? "))

# make a list to iterate over
number = [num]

# confirm we have a valid number
while num > 0:
    for n in number:
        # wait in between seconds
        time.sleep(1)
        num -= 1
        print(num)

if num <= 0:
    print("Done!")
