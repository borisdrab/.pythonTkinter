#Not Finished ?

with open("19_investicnyz.txt", "r") as subor:
    udaje = subor.readlines()
zoz = []
novy = {}
vysledok = 0
for i in udaje:
    zoz = i.strip().split()
    print(zoz)
    for j in zoz:
        novy = (zoz[1:])
        hodnota = int(novy[0])
        zisk = novy[1]  
        vysledok = (float(zisk)/hodnota)
        print(novy)
print(vysledok)