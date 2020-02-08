# vyukovy_program

Program bude na procvičování jednoduché matiky (+ - * /) a má různé složitosti (dohromady bude 3 úrovní složitosti).
Program bude generovat příklady a uživatel bude psát odpovědí. Uživatel bude mít 3 možnosti na zadání správné odpovědí, a pak po zadání 3 nesprávně program vypíše správnou odpověď.
Ze strány uživatele:
1) zadá úroveň složitosti
2) počet příkladů, které chce počítat
3) a pak jen řešit příklady

Program vygeneruje příklady, zkontroluje řešení a pak vypíše na konci počet bodů celkově za správně řešené úlohy a počet správně a špatně řešených úloh.


## Cíl

Cílem tohoto programu je procvičení sčítání/odečítání/násobení/dělení různě velkých čísel.


## Použití

Program se spouští spuštěním [vyukovy_program.py](vyukovy_program.py). Po spouštění tohoto programu se objeví okno s menu.
![menu_1](Pictures/menu_1.png)
Uživatel vybere nějakou kategorii y menu. Pak se objeví další menu s úrovní složitostí.
![menu_2](Pictures/menu_2.png)
Uživatel vybere úroveň složitostí, pak napíše počet příkladů, které chce počítat.
![menu_3](Pictures/menu_3.png)
Takto vypadá celé menu s předvyplněnými položkami.
![menu](Pictures/menu.png)
Pak začíná náhodné generování příkladú podle kategorii a úrovní složitostí.
![priklady](Pictures/priklady.png)
Po ukončení počítání program vyíiše prospěšnost: počet správně řešených příkladů y celkového počtů, počet získaných bodů a procentní úspěšnost.
![prospech](Pictures/prospech.png)

### Bodování

Každý příklad je za 3 body. Uživatel na 3 pokusy na řešení příkladu, každý další pokus -1 bod. Např. 
Za 3 body
![b_3](Pictures/b_3.png)
Za 2 body
![b_2](Pictures/b_2.png)
Za 1 bod
![b_1](Pictures/b_1.png)
Za 0 bodů
![b_0](Pictures/b_0.png)

### Kategorii

#### Sčítání "+"
* **1 - jednoduchý** - sčítání do 20
```python
...
def genSum1(countPr):
...
  for i in range(countPr):
        countAnswer = 3
        a = randint(0,20)
        b = randint(0, 20-a)
        x = a + b
        excercise = (f'{a} + {b} = ')
        vysledek = int(input(excercise))
...
```
* **2 - střední** - sčítání do 100
```python
...
def genSum2(countPr):
...
# liší se od 1 jen
        a = randint(0,100)
        b = randint(0, 100-a)
```
* **3 - složitý** - sčítání do 1000
```python
...
def genSum3(countPr):
...
# liší se od 1 a 2 jen
        a = randint(0,1000)
        b = randint(0, 1000-a)
```

#### oÖdečítání "-"
* **1 - jednoduchý** - odečítání do 20
* **2 - střední** - odečítání do 100
* **3 - složitý** - odečítání do 1000

Pro odečítání kód je stejný, odlišnost jen a - b.

#### Násobení "*"
* **1 - jednoduchý** - násobilka
```python
...
def genPro1(countPr):
...
  for i in range(countPr):
        countAnswer = 3
        a = randint(0,9)
        b = randint(0,9)
        x = a * b
        excercise = (f'{a} * {b} = ')
        vysledek = int(input(excercise))
...
```
* **2 - střední** - násobení dvoucíferné číslo na koncí s nulou a jednocíferné (0 až 9)
```python
...
def genPro2(countPr):
...
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
        vysledek = int(input(excercise))
...
```
* **3 - složitý** - násobení dvoucíferné číslo a jednocíferné (0 až 9)
```python
...
def genPro3(countPr):
...
# liší se jen geerováním čísel
            a = randint(10,99)
            b = randint(0,9)

```

#### Dělení "/"
* **1 - jednoduchý** - násobilka, ale dělení
```python
...
def genDiv1(countPr):
...
  for i in range(countPr):
        countAnswer = 3
        a = randint(1,9)
        b = randint(1,9)
        # k - výsledek násobení dvou náhodně vygenerovaných čísel
        k = a * b
        
        # náhodný výběr čísla, kterým budeme dělit
        if randint(0,1) == 0:
            x = a
            excercise = (f'{k} / {b} = ')
        else:
            x = b
            excercise = (f'{k} / {a} = ')
        vysledek = int(input(excercise))
...
```
* **2 - střední** - dělení jednocíferným číslem nebo dvoucíferným s nulou na konci 
```python
...
def genDiv2(countPr):
...
# liší se od 1 jen
        a = randrange(10,90,10)
        b = randint(1,9)
```

* **3 - složitý** - dělení jednocíferným číslem nebo dvoucíferným
```python
...
def genDiv3(countPr):
...
# liší se od 1 a 2 jen
        a = randint(10,99)
        b = randint(1,9)
```

