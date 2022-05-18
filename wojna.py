print("Gra w wojnę co turę zmiana")
import karty as k
import random
import collections
t=k.karty2A.copy()
random.shuffle(t)
g1=collections.deque()
g2=collections.deque()
stos1=collections.deque()
stos2=collections.deque()
wojna1=collections.deque()
wojna2=collections.deque()
x=random.randint(0,1)
tur=0
def wojna():
    global g1, g2, stos1, stos2, wojna1, wojna2
    ab = 0
    bb = 0
    if not g1:
        if stos1:
            g1 = stos1.copy()
            stos1.clear()
        else:
            ab = 1
    if not g2:
        if stos2:
            g2 = stos2.copy()
            stos2.clear()
        else:
            bb = 1
    if ab == 0 and bb == 0:
        wojna1.append(g1.popleft())
        wojna2.append(g2.popleft())
        if not g1:
            if stos1:
                g1 = stos1.copy()
                stos1.clear()
            else:
                ab = 1
        if not g2:
            if stos2:
                g2 = stos2.copy()
                stos2.clear()
            else:
                bb = 1
        if ab == 0 and bb == 0:
            wojna1.append(g1.popleft())
            wojna2.append(g2.popleft())
        elif ab == 0:
            wojna1.append(g1.popleft())
            if not g1:
                g1 = stos1.copy()
                stos1.clear()
            wojna2.append(g1.popleft())
        elif bb == 0:
            wojna1.append(g2.popleft())
            if not g2:
                g2 = stos2.copy()
                stos2.clear()
            wojna2.append(g2.popleft())
    elif ab == 0:
        wojna1.append(g1.popleft())
        if not g1:
            g1 = stos1.copy()
            stos1.clear()
        wojna2.append(g1.popleft())
        if not g1:
            g1 = stos1.copy()
            stos1.clear()
        wojna1.append(g1.popleft())
        if not g1:
            g1 = stos1.copy()
            stos1.clear()
        wojna2.append(g1.popleft())
    elif bb == 0:
        wojna1.append(g2.popleft())
        if not g2:
            g2 = stos2.copy()
            stos2.clear()
        wojna2.append(g2.popleft())
        if not g2:
            g2 = stos2.copy()
            stos2.clear()
        wojna1.append(g2.popleft())
        if not g2:
            g2 = stos2.copy()
            stos2.clear()
        wojna2.append(g2.popleft())
    if wojna1[-1].value>wojna2[-1].value:
        return -1
    elif wojna1[-1].value<wojna2[-1].value:
        return 1
    elif not g1 and not g2 and not stos1 and not stos2:
        return 0
    else: wojna()
for i in range(0, 24, 2):
    g1.appendleft(t[i])
    g2.appendleft(t[i+1])
while g1 and g2:
    tur+=1
    a1=g1.popleft()
    b1=g2.popleft()
    if a1.value>b1.value:
        print("wygrywa turę gracz 1    karty: ", a1.value, b1.value)
        if x==1:
            stos1.append(a1)
            stos1.append(b1)
        else:
            stos1.append(b1)
            stos1.append(a1)
        x=0
    elif a1.value<b1.value:
        print("wygrywa turę gracz 2    karty: ", a1.value, b1.value)
        if x==1:
            stos2.append(a1)
            stos2.append(b1)
        else:
            stos2.append(b1)
            stos2.append(a1)
        x=1
    else:
        wojna1.append(a1)
        wojna2.append(b1)
        result = wojna()
        if result==0:
            print("remis koniec gry")
            break
        elif result==-1:
            print("wojne wygrywa gracz 1")
            for _ in range(len(wojna1)):
                stos1.append(wojna1.popleft())
                stos1.append(wojna2.popleft())
            x=0
        else:
            print("wojne wygrywa gracz 2")
            for _ in range(len(wojna1)):
                stos2.append(wojna1.popleft())
                stos2.append(wojna2.popleft())
            x=1
    if not g1:
        g1=stos1.copy()
        stos1.clear()
    if not g2:
        g2=stos2.copy()
        stos2.clear()
if g1:
    print("wygrywa gracz 1")
if g2:
    print("wygrywa gracz 2")
print("było", tur, "tur")








