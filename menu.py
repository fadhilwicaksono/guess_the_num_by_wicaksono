def screen():
    print("==================================================")
    print("|            GUESS THE NUMBER GAME               |")
    print("==================================================")
    print("|                                                |")
    print("|                                                |")
    print("|         click any keyboard to continue         |")
    print("|                                                |")
    print("|                                                |")
    print("|================================================|")
    input("")

def menu():
    print("==================================================")
    print("|            GUESS THE NUMBER GAME               |")
    print("==================================================")
    print("|        1. Guess The Number                     |")
    print("|        2. Guess The Winner                     |")
    print("|        3. Exit                                 |")

    print("|================================================|")
    print("==> ", end="")
    answer=int(input(""))
    return answer


