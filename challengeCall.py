import random

def my_challenge():
    print("Will you need to roll Challenge dice?")
    challenge_answer = input("Answer yes/no: ").upper()
    
    if challenge_answer == "YES":
        challenge = True
    elif challenge_answer == "NO":
        challenge = False
    else:
        print("Please answer \"Yes\" or \"No\"")
        challenge = my_challenge()
    
    return challenge