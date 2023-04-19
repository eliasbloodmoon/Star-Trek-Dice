import random
from focusCall import *
from momentumCall import *
from challengeCall import *

def main():
    try:
        focus = my_focus()
        comp_range = 21 - int(input("What is your Complication Range? "))
        number_of_dice = int(input("How many dice are you rolling? "))
        attribute = int(input("What is your Attribute rating? "))
        discipline = int(input("What is your Discipline rating? "))
        rolls = [random.randint(1, 20) for _ in range(number_of_dice)]
        difficulty = int(input("What is your difficulty? "))
        successes = 0
        complications = 0
        for roll in rolls:
            if (focus and roll <= discipline) or roll == 1:
                successes += 2
            elif roll <= attribute + discipline:
                successes += 1
            if roll >= comp_range:
                complications += 1
        if successes >= difficulty:
            momentum = successes - difficulty
            print(f"You succeeded with {momentum} momentum and {complications} complications.")
            challenge = my_challenge()
            if momentum > 0:
                momentum_calculator(momentum, challenge)
        else:
            print(f"You failed with {complications} complications.")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()