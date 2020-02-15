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
    operace = "+"
    if level == 1:
        u = 0
        v = 20
        w = 1
    elif level == 2:
        u = 20
        v = 100
        w = 1
    elif level == 3:
        u = 100
        v = 1000
        w = 1
    generator.Pocet(Priklady, u, v, w, operace)

def Difference():
    operace = "-"
    level == 1:
        u = 0
        v = 20
        w = 1
    elif level == 2:
        u = 20
        v = 100
        w = 1
    elif level == 3:
        u = 100
        v = 1000
        w = 1
    generator.Pocet(Priklady, u, v, w, operace)

def Product():
    operace = "*"
    if level == 1:
        u = 0
        v = 9
        w = 1
    elif level == 2:
        u = 10
        v = 90
        w = 10
    elif level == 3:
        u = 10
        v = 99
        w = 1
    generator.Pocet(Priklady, u, v, w, operace)

def Division():
    operace = "/"
    if level == 1:
        u = 1
        v = 9
        w = 1
    elif level == 2:
        u = 10
        v = 90
        w = 10
    elif level == 3:
        u = 10
        v = 99
        w = 1
    generator.Pocet(Priklady, u, v, w, operace)

print("VÝUKOVÝ PROGRAM")
Menu()



