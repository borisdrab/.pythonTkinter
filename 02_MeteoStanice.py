with open("02_MeteoStanicky.txt", "r") as subor:
    print(f"Uvedenych zaznamov je: {len(subor.readlines())}")

with open("02_MeteoStanicky.txt", "r") as subor:
    udaje = subor.readlines()
    zoz = []
    for i in udaje:
        zoz.append(i.strip().split())

zoz_tep = []
for i in zoz:
    zoz_tep.append(i[3])
print(f"Namerane teploty su: {zoz_tep}")

zoz_max = []
for i in zoz_tep:
    if i[0] == "+":
        zoz_max.append(i)
print(f"Najvyssia namerana teplota je: +{max(zoz_max)}")

for i in zoz:
    if i[3] == float(max(zoz_max)):
        print(f"Najvyssia teplota bola namerana na: {i[0]}")


zoz_priemer = []
for i in zoz:
    zoz_priemer.append(float(i[3]))
priemer = sum(zoz_priemer)/len(zoz_priemer)
print(f"Primer teploty je: {priemer.round(2)}")