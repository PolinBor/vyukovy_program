from random import randint
import sys
import generator

def Menu():
    # MENU
    print("----------------")
    print("Sčítanání - 1")
    print("Odečítání - 2")
    print("Násobení  - 3")
    print("Dělení    - 4")
    print("KONEC     - 0")
    print("-----------------")
    global menu 
    menu = int(input("Vyber kategorii, kterou chceš počítat: "))
    if menu == 0:
        exit()
    elif menu > 4:
        print("Zadej platnou kategorii")
        Menu()
    else:
        Level()

def Level():
    print("------------------")
    print("Úroveň složitosti:")
    print("Jednoduchý - 1")
    print("Střední    - 2")
    print("Složitý    - 3")
    print("KONEC      - 0")
    print("------------------")
    global level
    level = int(input("Vyber úroveň složitosti: "))
    if level == 0:
        exit()
    elif level > 3:
        print("Zadej platnou kategorii")
        Level()
    else:
        CountRep()

def CountRep():
    # množstvi příkladů
    global Priklady
    print("-----------------------------")
    Priklady = int(input("Kolik příkladů chceš počítat? "))
    print("-----------------------------")
    print("-----------------------------")
    
    if menu == 1:
        Sum()
        Menu()
    elif menu == 2:
        Difference()
        Menu()
    elif menu == 3:
        Product()
        Menu()
    elif menu == 4:
        Division()
        Menu()

def Sum():
    if level == 1:
        generator.genSum1(Priklady)
    elif level == 2:
        generator.genSum2(Priklady)
    elif level == 3:
        generator.genSum3(Priklady)
    return

def Difference():
    if level == 1:
        generator.genDif1(Priklady)
    elif level == 2:
        generator.genDif2(Priklady)
    elif level == 3:
        generator.genDif3(Priklady)
    return

def Product():
    if level == 1:
        generator.genPro1(Priklady)
    elif level == 2:
        generator.genPro2(Priklady)
    elif level == 3:
        generator.genPro3(Priklady)
    return

def Division():
    if level == 1:
        generator.genDiv1(Priklady)
    elif level == 2:
        generator.genDiv2(Priklady)
    elif level == 3:
        generator.genDiv3(Priklady)
    return

print("VÝUKOVÝ PROGRAM")
Menu()



