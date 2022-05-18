class karta:
    def __init__(self, value, color):
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
def wypisz_karte(obj):
    colors=["Wino", "Czerwień", "Żołądź", "Dzwonek"]
    val=["Walet", "Dama", "Król", "As"]
    if obj.value>10:
        print(val[obj.value-11], " ", colors[obj.color])
    else:
        print(val[obj.value], " ", colors[obj.color])