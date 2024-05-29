import random   
def movimento_tartaruga():
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        return 3
    elif 6 <= i <= 7:
        return -6
    else:
        return 1
def movimento_lepre():
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        return 0
    elif 3 <= i <= 4:
        return 9
    elif i == 5:
        return -12
    elif 6 <= i <= 8:
        return 1
    else:
        return -2

def visualizza_posizioni(tartaruga, lepre):
    for i in range(1, 71):
        if i == tartaruga == lepre:
            print('OUCH!!!', end='')
        elif i == tartaruga:
            print('T', end='')
        elif i == lepre:
            print('H', end='')
        else:
            print('_', end='')
    print()
def gara():
    tartaruga = lepre = 1
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        tartaruga = max(1, tartaruga + movimento_tartaruga())
        lepre = max(1, lepre + movimento_lepre())
        visualizza_posizioni(tartaruga, lepre)
        if tartaruga >= 70 and lepre >= 70:
            print("IT'S A TIE.")
            break
        elif tartaruga >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif lepre >= 70:
            print("HARE WINS || YUCH!!!")
            break
gara()
