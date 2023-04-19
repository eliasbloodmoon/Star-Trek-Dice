import random

def momentum_calculator(m, c):

    try:

        answer = None
        input_ = input
        print = print
        int = int
        
        rand = random.Random()
        
        if c:
            print("How many challenge dice are we rolling?")
            challenge_dice = int(input_())
            c_rolls = []
            for i in range(challenge_dice):
                c_rolls.append(rand.randint(1, 6))
            
            print("Your challenge rolls are: ", end="")
            for i in c_rolls:
                if i == 1 or i == 2:
                    print(f"{i} ", end="")
                elif i == 3 or i == 4:
                    print("Blank ", end="")
                elif i == 5 or i == 6:
                    print("Effect ", end="")
            
            print()
        
        while m != 0:
            print("Momentum Spend Choices")
            print("1: Basic Spends")
            if c:
                print("2: Combat Spends")
                print("3: Extended Task Spends")
            print("0: Bank Momentum")
            
            answer = int(input_())
            
            if answer == 1:
                basic_num = 5
                while basic_num != 0 and m > 0:
                    print("Basic Momentum Spends")
                    print("1: Create Advantage (2 cost)")
                    print("2: Obtain Information (1 cost, Repeatable)")
                    print("You have " + str(m) + " momentum")
                    print("Enter 0 to return")
                    
                    basic_num = int(input_())
                    if basic_num == 1:
                        print("Create an Advantage based on your roll")
                        m -= 2
                    elif basic_num == 2:
                        print("Ask a question of the GM")
                        m -= 1
                    elif basic_num == 0:
                        print("Return to main menu")
                    else:
                        print("Please insert a proper menu response")
            
            if c and answer == 2:
                combat_num = 9
                while combat_num != 0 and m > 0:
                    print("Combat Task Spends")
                    print("1: Bonus Damage (1 cost, Repeatable)")
                    print("2: Disarm (2 cost)")
                    print("3: Extra Minor Action (1 cost, Repeatable)")
                    print("4: Keep the Initiative (2 cost)")
                    print("5: Penetrate Defenses (1 cost, Repeatable)")
                    print("6: Reroll Damage (1 cost)")
                    print("7: Secondary Target (2 cost)")
                    print("8: Swift Task (2 cost)")
                    print("You have " + str(m) + " momentum")
                    
                    combat_num = int(input_())
                    if combat_num == 1:
                        print("One extra damage dealt")
                        m -= 1
                    elif combat_num == 2:
                        print("Your opponent has been disarmed, their weapon within their Reach")
                        m -= 2
                    elif combat_num == 3:
                        print("Perform an extra Minor Action")
                        m -= 1
                    elif combat_num == 4:
                        print("Your team keeps the initiative")
                        m -= 2
                    elif combat_num == 5:
                        print("Ignore 2 of your target's Resistance")
                        m -= 1
                    elif combat_num == 6:
                        print("Your challenge rolls are: ", end="")
                        x = 1
                        for i in c_rolls:
                            print(f"{x}: ", end="")
                            x += 1
                            if i == 1 or i == 2:
                                print(f"{i}")
                            elif i == 3 or i == 4:
                                print("Blank")
                            elif i == 5 or i == 6:
                                print("Effect")
                        print()
                        print("How would many dice would you like to reroll?")
                        reroll = int(input())
                        print("Which dice would you like to reroll?")
                        while reroll > 0:
                            chosenDie = int(input())
                            c_rolls[chosenDie] = rand.randint(1,6)
                        print("Your challenge rolls are: ", end="")
                        for i in c_rolls:
                            if i == 1 or i == 2:
                                print(f"{i} ", end="")
                            elif i == 3 or i == 4:
                                print("Blank ", end="")
                            elif i == 5 or i == 6:
                                print("Effect ", end="")
                        print()
                        m -= 1
                    elif combat_num == 7:
                        print("A second target withing Reach of your target is also affected by the attack, and suffers half damage rounding down")
                        m -= 2
                    elif combat_num == 8:
                        print("Do one normal task as a minor action, increasing the difficulty due to speed")
                        m -= 2
                    elif combat_num == 0:
                        print("Return to Main Menu")
                    else:
                        print("Please insert a proper menu response")


            if c and answer == 3:
                extended_num = 4
                while extended_num != 0 and m > 0:
                    print("Extended Task Spends")
                    print("1: Additional Work (1 cost, Repeatable)")
                    print("2: Pierce Resistance (1 cost, Repeatable)")
                    print("3: Reroll Dice (1 cost, Repeatable)")
                    print("You have " + str(m) + " momentum")
                    print("Enter 0 to return")

                    extended_num = int(input())
                    if extended_num == 1:
                        print("Increase work on this Task by 1")
                        m -= 1
                    elif extended_num == 2:
                        print("Reduce resistance by 2 for this roll")
                        m -= 1
                    elif extended_num == 3:
                        print("Your challenge rolls are: ", end="")
                        x = 1
                        for i in c_rolls:
                            print(f"{x}: ", end="")
                            x += 1
                            if i == 1 or i == 2:
                                print(f"{i}")
                            elif i == 3 or i == 4:
                                print("Blank")
                            elif i == 5 or i == 6:
                                print("Effect")
                        print()
                        print("How would many dice would you like to reroll?")
                        reroll = int(input())
                        print("Which dice would you like to reroll?")
                        while reroll > 0:
                            chosenDie = int(input())
                            c_rolls[chosenDie] = rand.randint(1,6)
                        print("Your challenge rolls are: ", end="")
                        for i in c_rolls:
                            if i == 1 or i == 2:
                                print(f"{i} ", end="")
                            elif i == 3 or i == 4:
                                print("Blank ", end="")
                            elif i == 5 or i == 6:
                                print("Effect ", end="")
                        print()
                    elif extended_num == 0:
                        print("Return to Main Menu")
                    else:
                        print("Please insert a proper menu response")
    except ValueError:
        print("Please enter a valid integer.")