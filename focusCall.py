def my_focus():
    while True:
        focus_answer = input("Do you have an applicable focus? Answer yes/no ")
        if focus_answer.upper() == "YES":
            return True
        elif focus_answer.upper() == "NO":
            return False
        else:
            print("Please answer \"Yes\" or \"No\".")