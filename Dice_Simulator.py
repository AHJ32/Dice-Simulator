import random # This module lets us choose random numbers

class Dices:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 12)

choice = int(input("Do you want 1 dice or 2 dice to roll?\n"))

if choice == 1:
    print(f"you rolled {Dices.dice1}")
elif choice == 2:
    print(f"you rolled {Dices.dice2}")

'''
This gives user the option to choose the amount of dices

choice = int(input("How many dices you want to roll?\n"))
dice = random.randint(1, 6 * choice)
print(f"you rolled {dice}")
'''