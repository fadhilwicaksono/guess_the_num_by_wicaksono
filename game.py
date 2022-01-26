import menu
import os
from pack import gtn_set, gtn, gtw

answer_menu = 1
while answer_menu != 3:
    
    if answer_menu == 1:
        screen = menu.menu()
        answer = int(screen)
        os.system("cls")
        if answer == 1:
            gtn_set()
        elif answer == 2:
            gtw()
        elif answer == 3:
            answer_menu=3
            break
    
os.system("cls")