import random
import menu
import os
############|RULES|#############################################
def rules():
    print("You only have 3 chances to guess the number")

############|GAME NO 1|#############################################
def gtn():
    i = 1
    gtn_number = random.randint(0,9)
    chance = 3
    while i < 4:
        answer_gtn = input("Guess the number(0-9): ")
        answer_gtn = int(answer_gtn)
        chance -= 1
        if answer_gtn == gtn_number:
            os.system("cls")
            print("Congratulations You Win The Game")
            print("You have great instinct")
            break
        else:
            os.system("cls")
            print((f"You wrong! your chance {chance}"))
        i += 1
        if chance == 0:
                os.system("cls")
                print("YOU HAVE LOST THE GAME!")
                break
    os.system("pause")
    os.system("cls")
    


#########################|GAMEPLAY|##########################################
def gtn_set():
    rules()
    digit_gtn = input("Ready to play the game ? (y/n)")
    
    while digit_gtn != "n":
        
        if digit_gtn == "y":
            os.system("cls") 
            print("The number will be between 0-9")
            gtn()
            break
        else:
            print("You have input an invalid number")
            break
    
        
def gtw(): ##
    rules()
    nominations = input("How many nominations to be on the list : ")
    nominations = int(nominations)
    list = []
    i = 0
    while i < nominations:
        new_name = input("Name of the nomination : ")
        list.append(new_name)
        i += 1
    def nom_list():
        i = 0   
        print("The nominations list : ")
        while i < len(list):
            print(f"{i+1}. {list[i]}")
            i += 1

    i = 0
    winner = random.choice(list)
    chance = 3
    
    while i < 3:
        nom_list()
        answer_gtw = input("Guess the winner : ")
        answer_gtw = answer_gtw.lower()
        chance -= 1
        if answer_gtw == winner.lower():
            os.system("cls")
            print("Congratulations You Win The Game")
            print("You have great instinct")
            print(f"THE WINNER OF THE NOMINATIONS IS {winner}")
            break
        else:
            os.system("cls")
            print((f"You wrong! your chance {chance}"))
        i += 1
        if chance == 0:
                os.system("cls")
                print("YOU HAVE LOST THE GAME!")
                break
    os.system("pause")
    os.system("cls")
            
            
        

    



