from random import randint, randrange

sPoints = []
sCountEx = []

def genSum1(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(0,20)
        b = randint(0, 20-a)
        x = a + b
        excercise = (f'{a} + {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y
    
    Vysledky(countEx1, countPr, Points1, maxPoints)

def genSum2(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(20, 100)
        b = randint(0, 100-a)
        x = a + b
        excercise = (f'{a} + {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)
    
    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y
    
    Vysledky(countEx1, countPr, Points1, maxPoints)

def genSum3(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(100, 1000)
        b = randint(0, 1000-a)
        x = a + b
        excercise = (f'{a} + {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)
    
    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y
    
    Vysledky(countEx1, countPr, Points1, maxPoints)        

def genDif1(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(0,20)
        b = randint(0, a)
        x = a - b
        excercise = (f'{a} - {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genDif2(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(20,100)
        b = randint(0, a)
        x = a - b
        excercise = (f'{a} - {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genDif3(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(100,1000)
        b = randint(0, a)
        x = a - b
        excercise = (f'{a} - {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genPro1(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(0,9)
        b = randint(0,9)
        x = a * b
        excercise = (f'{a} * {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genPro2(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        # náhodné vybírání, jaké číslo bude na prvním místě jednociferné nebo dvouciferné
        if randint(0,1) == 0:
            a = randrange(10,90,10)
            b = randint(0,9)
        else:
            a = randint(0,9)
            b = randrange(10,90,10)
        x = a * b
        excercise = (f'{a} * {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genPro3(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        if randint(0,1) == 0:
            a = randint(10,99)
            b = randint(0,9)
        else:
            a = randint(0,9)
            b = randint(10,99)
        x = a * b
        excercise = (f'{a} * {b} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genDiv1(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(1,9)
        b = randint(1,9)
        k = a * b
        
        if randint(0,1) == 0:
            x = a
            excercise = (f'{k} / {b} = ')
        else:
            x = b
            excercise = (f'{k} / {a} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genDiv2(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randrange(10,90,10)
        b = randint(1,9)
        k = a * b
        
        if randint(0,1) == 0:
            x = a
            excercise = (f'{k} / {b} = ')
        else:
            x = b
            excercise = (f'{k} / {a} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def genDiv3(countPr):
    sPoints.clear()
    sCountEx.clear()

    countEx = 0
    Points = 0
    maxPoints = countPr * 3
    for i in range(countPr):
        countAnswer = 3
        a = randint(10,99)
        b = randint(1,9)
        k = a * b
        
        if randint(0,1) == 0:
            x = a
            excercise = (f'{k} / {b} = ')
        else:
            x = b
            excercise = (f'{k} / {a} = ')
        vysledek = int(input(excercise))
        Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints)

    countEx1 = 0
    Points1 = 0
    for z in sPoints:
        Points1 += z
    for y in sCountEx:
        countEx1 += y

    Vysledky(countEx1, countPr, Points1, maxPoints)

def Reseni(vysledek, x, Points, countAnswer, countEx, countPr, maxPoints):
    if vysledek == x:
        print("Správně")
        print("-----------------------------")
        countAnswer = 3
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
    
    
    sPoints.append(Points)
    sCountEx.append(countEx)
    return Points, countEx

def Vysledky(countEx1, countPr, Points1, maxPoints):
    print(countEx1, "/", countPr)
    print(Points1, "/", maxPoints)
    print("Prospěšnost: ", (Points1 * 100 / maxPoints), "%")
    print()
