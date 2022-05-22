class karta:
    def __init__(self, value, color, numer=0):
        self.numer=numer
        self.value=value
        self.color=color
karty2A=[]
for i in range(4):
    for j in range(2, 15):
        karty2A.append(karta(j, i))
karty9A=[]
for i in range(4):
    for j in range(9, 15):
        karty9A.append(karta(j, i))
karty_tysiac=[]
for i in range(4):
    for j in range(9, 15):
        if j==9:
            karty_tysiac.append(karta(0, i, j))
        elif j==10:
            karty_tysiac.append(karta(10, i, j))
        elif j==14:
            karty_tysiac.append(karta(11, i, j))
        else:
            karty_tysiac.append(karta(j-9, i, j))

def wypisz_karte(obj):
    colors=["W", "C", "Z", "D"]
    val=["W", "D", "K", "A"]
    if obj.numer>10:
        print(val[obj.numer-11], colors[obj.color], sep="", end=" ")
    else:
        print(obj.numer, colors[obj.color], sep="", end=" ")