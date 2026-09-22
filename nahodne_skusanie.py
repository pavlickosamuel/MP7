import random
po = int(input("Počet otázok: "))
ps = int(input("Počet študentov: "))

studenti = []
otazky = []
parne = []
neparne = []

for i in range(1,po+1):
    otazky.append(i)
    if i %2 == 0:
        parne.append(i)
    else:
        neparne.append(i)
for a in range(1,ps+1):
    studenti.append(a)

if po<ps:
    print("málo otazok")
else:
    random.shuffle(studenti)
    random.shuffle(otazky)
    random.shuffle(parne)
    random.shuffle(neparne)
    nove_o = []
    for i in range(ps):
        if i %2 == 0:
            nove_o.append(parne.pop(0))
        else:
            nove_o.append(neparne.pop(0))
    otazky = nove_o
    for j in range(ps):
        print(f"{j+1}.študent - {studenti[j]} - otázka {otazky[j]}")