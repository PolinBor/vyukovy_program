from random import randint, randrange

sPoints = []
sCountEx = []

def Pocet(countPr, u, v, w, operace):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3

    vysledek = 0
    x = 0
    countAnswer = 3

    if operace == "+":
        for _ in range(countPr):
            vysledek, x = genSum(u, v)
            Reseni(vysledek, x, Points, countAnswer, countEx)
    elif operace == "-":
        for _ in range(countPr):
            vysledek, x = genDif(u, v)
            Reseni(vysledek, x, Points, countAnswer, countEx)
    elif operace == "*":
        for _ in range(countPr):
            vysledek, x = genPro(u, v, w)
            Reseni(vysledek, x, Points, countAnswer, countEx)
    elif operace == "/":
        for _ in range(countPr):
            vysledek, x = genDiv(u, v, w)
            Reseni(vysledek, x, Points, countAnswer, countEx)
    
    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y
    
    Vysledky(countEx1, countPr, Points1, maxPoints)

def genSum(u, v):
    a = randint(u,v)
    b = randint(0, v-a)
    x = a + b
    excercise = (f'{a} + {b} = ')
    vysledek = int(input(excercise))        
    return vysledek, x           

def genDif(u, v):
    a = randint(u,v)
    b = randint(0, a)
    x = a - b
    excercise = (f'{a} - {b} = ')
    vysledek = int(input(excercise))        
    return vysledek, x

def genPro(u, v, w):
    if randint(0,1) == 0:
        a = randrange(u, v, w)
        b = randint(0,9)
    else:
        a = randint(0,9)
        b = randrange(u, v, w)
    x = a * b
    excercise = (f'{a} * {b} = ')
    vysledek = int(input(excercise))
    return vysledek, x

def genDiv(u, v, w):
    a = randrange(u, v, w)
    b = randint(1,9)
    k = a * b
        
    if randint(0,1) == 0:
        x = a
        excercise = (f'{k} / {b} = ')
    else:
        x = b
        excercise = (f'{k} / {a} = ')
    vysledek = int(input(excercise))
    return vysledek, x

def Reseni(vysledek, x, Points, countAnswer, countEx):
    if vysledek == x:
        print("Správně")
        print("-----------------------------")
        countAnswer = countAnswer
        Points += countAnswer
        countEx += 1
    elif vysledek != x:
        for j in range(3):
            if vysledek == x:
                print("Správně")
                print("-----------------------------")
                countAnswer = countAnswer
                Points += countAnswer
                break
            elif vysledek != x:
                if vysledek > x:
                    countAnswer -= 1
                    if countAnswer == 0:
                        break
                    else:
                        vysledek = int(input("Zkus si tipnout nižší číslo: "))
                    
                elif vysledek < x:
                    countAnswer -= 1
                    if countAnswer == 0:
                        break
                    else:
                        vysledek = int(input("Zkus si tipnout větší číslo: "))
                
        if countAnswer != 0:
            countEx += 1
        elif countAnswer == 0:
            print("Správná odpověď je: ", x)
            print("-----------------------------")
    
    
    sPoints.append(Points)
    sCountEx.append(countEx)
    return Points, countEx

def Vysledky(countEx1, countPr, Points1, maxPoints):
    print(countEx1, "/", countPr)
    print(Points1, "/", maxPoints)
    print("Prospěšnost: ", (Points1 * 100 / maxPoints), "%")
    print()
