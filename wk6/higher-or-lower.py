# Title: Wk6 Task 1 - Higher or Lower
# Author: Braedyn Murtagh (braedynm)
# Date: 2023-03-08
#
# Asks the user for a maximum number, and then
# repeatedly asks for a guess, providing "Higher" or "Lower"
# until the user correctly guesses the number.
import random


def getMax():
    while True:
        res = input("Input maximum number (default 100): ")
        if len(res) == 0:
            return 101
        elif not res.isnumeric():
            print("Invalid Input")
        else:
            v = int(res)
            if v < 10:
                print("Number must be greater than 10.")
            else:
                return v+1


tries = 0
maxval = getMax()
val = random.randint(1, maxval)
while True:
    res = input("Input Guess: ")
    if not res.isnumeric():
        print("Invalid Input")
    else:
        num = int(res)
        if num not in range(1, maxval):
            print(f"Number must be between 1 and {maxval-1}")
        else:
            tries += 1
            if num > val:
                print("Lower")
            elif num < val:
                print("Higher")
            else:
                print(f"Correct! Got the correct number in {tries} tries.")
                break
