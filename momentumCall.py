import random

def momentum_calculator(m, c):
    answer = None
    input_ = input
    print_ = print
    int_ = int
    
    rand = random.Random()
    
    if c:
        print_("How many challenge dice are we rolling?")
        challenge_dice = int_(input_())
        c_rolls = []
        for i in range(challenge_dice):
            c_rolls.append(rand.randint(1, 6))
        
        print_("Your challenge rolls are: ", end="")
        for i in c_rolls:
            if i == 1:
                print_("1 ", end="")
            elif i == 2:
                print_("2 ", end="")
            elif i == 3 or i == 4:
                print_("Blank ", end="")
            elif i == 5 or i == 6:
                print_("Effect ", end="")
        
        print_()
    
    while m != 0:
        print_("Momentum Spend Choices")
        print_("1: Basic Spends")
        if c:
            print_("2: Combat Spends")
            print_("3: Extended Task Spends")
        print_("0: Bank Momentum")
        
        answer = int_(input_())
        
        if answer == 1:
            basic_num = 5
            while basic_num != 0 and m > 0:
                print_("Basic Momentum Spends")
                print_("1: Create Advantage (2 cost)")
                print_("2: Obtain Information (1 cost)")
                print_("You have " + str(m) + " momentum")
                print_("Enter 0 to return")
                
                basic_num = int_(input_())
                if basic_num == 1:
                    print_("Create an Advantage based on your roll")
                    m -= 2
                elif basic_num == 2:
                    print_("Ask a question of the GM")
                    m -= 1
                elif basic_num == 0:
                    print_("Return to main menu")
                else:
                    print_("Please insert a proper menu response")
        
        if c and answer == 2:
            pass