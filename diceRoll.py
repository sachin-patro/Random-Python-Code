import random

min = 1
max = 6

def roll(min, max):
    while True:
        print("Rolling the dice...")
        print(f"Your number is {random.randint(min, max)}")
        rollAgain = input("Do you want to roll again? (Y)es or (N)o? ")
        if rollAgain.upper() == "N":
            break

        elif rollAgain.lower() == "n":
            print("Thanks for playing!")

            break


roll(min, max)
