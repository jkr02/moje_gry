import collections
import random

import karty
print("WITAJ W GRZE KARCIANEJ TYSIAC!!!\naby zglosic meldunek:\nw - meldunek wino\nc - meldunek czerwo\nz - meldunek zoladz\nd - meldunek dzwonek")
def meldunek(gracz, kolor):
    global g1, g2
    dama=0
    krol=0
    for i in range(len(gracz)):
        if gracz[i].numer==12 and gracz[i].color==kolor:
            dama=1
        if gracz[i].numer==13 and gracz[i].color==kolor:
            krol=1
    if krol and dama:
        return True
    return False

g1=[]
g2=[]
talia=collections.deque()
t=karty.karty_tysiac.copy()
print("TASOWANIE...")
random.shuffle(t)
for i in range(len(t)):
    talia.append(t[i])
del t
print("ROZDAWANIE...")
for i in range(6):
    g1.append(talia.popleft())
    g2.append(talia.popleft())
x=random.randint(0,1)
wynik_a=0
wynik_b=0
tromf=-1
while g1 and g2:
    def ruch(gracz, p):
        print("RUCH GRACZA NR", p)
        for i in range(len(gracz)):
            karty.wypisz_karte(gracz[i])
        print()
        while True:
            s=input("wybierz karte> ")
            if s=="w" or s=="c" or s=="z" or s=="d":
                if s=="w":
                    s=0
                if s=="c":
                    s=1
                if s=="z":
                    s=2
                if s=="d":
                    s=3
                if not meldunek(gracz, s):
                    print("Nie masz kart spelniajacych meldunek")
                    continue
                else:
                    for i in range(len(gracz)):
                        if gracz[i].numer==12 and gracz[i].color==s:
                            return gracz.pop(i), s
            elif int(s)>=0 and int(s)<=len(gracz):
                return gracz.pop(int(s)), None
            else:
                print("podaj liczbe z zakresu 0-",len(gracz)-1," lub w, c, z, d", sep="")
    if x == 0:
        a = ruch(g1, 1)
        if a[1]!=None:
            if tromf==-1:
                tromf=a[1]
            if a[1]==0:
                print("meldunek winny za 80")
                wynik_a+=80
            elif a[1]==1:
                print("meldunek czerwo za 60")
                wynik_a+=60
            elif a[1]==2:
                print("meldunek zolenny za 100")
                wynik_a+=100
            elif a[1]==3:
                print("meldunek dzwonkowy za 40")
                wynik_a+=40
        b = ruch(g2,2)
        if b[1]!=None:
            if tromf == -1:
                tromf = b[1]
            if b[1] == 0:
                print("meldunek winny za 80")
                wynik_b += 80
            elif b[1] == 1:
                print("meldunek czerwo za 60")
                wynik_b += 60
            elif b[1] == 2:
                print("meldunek zolenny za 100")
                wynik_b += 100
            elif b[1] == 3:
                print("meldunek dzwonkowy za 40")
                wynik_b+=40
        if b[0].color==tromf and a[0].color!=tromf:
            print("ture wygrywa gracz 2")
            x=1
            wynik_b+=a[0].value+b[0].value
            if talia:
                g2.append(talia.popleft())
                g1.append(talia.popleft())
            continue
        elif b[0].color==a[0].color:
            if b[0].value>a[0].value:
                print("ture wygrywa gracz 2")
                x=1
                wynik_b+=a[0].value+b[0].value
                if talia:
                    g2.append(talia.popleft())
                    g1.append(talia.popleft())
                continue
            else:
                print("ture wygrywa gracz 1")
                x=0
                wynik_a+=a[0].value+b[0].value
                if talia:
                    g1.append(talia.popleft())
                    g2.append(talia.popleft())
                continue
        else:
            print("wygrywa gracz 1")
            x=0
            wynik_a+=a[0].value+b[0].value
            if talia:
                g1.append(talia.popleft())
                g2.append(talia.popleft())
    else:
        b = ruch(g2,2)
        if b[1]!=None:
            if tromf == -1:
                tromf = b[1]
            if b[1] == 0:
                print("meldunek winny za 80")
                wynik_b += 80
            elif b[1] == 1:
                print("meldunek czerwo za 60")
                wynik_b += 60
            elif b[1] == 2:
                print("meldunek zolenny za 100")
                wynik_b += 100
            elif b[1] == 3:
                print("meldunek dzwonkowy za 40")
                wynik_b+=40
        a = ruch(g1,1)
        if a[1]!=None:
            if tromf==-1:
                tromf=a[1]
            if a[1]==0:
                print("meldunek winny za 80")
                wynik_a+=80
            elif a[1]==1:
                print("meldunek czerwo za 60")
                wynik_a+=60
            elif a[1]==2:
                print("meldunek zolenny za 100")
                wynik_a+=100
            elif a[1]==3:
                print("meldunek dzwonkowy za 40")
                wynik_a+=40
        if a[0].color==tromf and b[0].color!=tromf:
            print("ture wygrywa gracz 1")
            x=0
            wynik_a+=a[0].value+b[0].value
            if talia:
                g1.append(talia.popleft())
                g2.append(talia.popleft())
            continue
        elif b[0].color==a[0].color:
            if a[0].value>b[0].value:
                print("ture wygrywa gracz 1")
                x=0
                wynik_a+=a[0].value+b[0].value
                if talia:
                    g1.append(talia.popleft())
                    g2.append(talia.popleft())
                continue
            else:
                print("ture wygrywa gracz 2")
                x=1
                wynik_b+=a[0].value+b[0].value
                if talia:
                    g2.append(talia.popleft())
                    g1.append(talia.popleft())
                continue
        else:
            print("wygrywa gracz 2")
            x=1
            wynik_b+=a[0].value+b[0].value
            if talia:
                g2.append(talia.popleft())
                g1.append(talia.popleft())
