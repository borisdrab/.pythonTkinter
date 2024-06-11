zoznam = []

with open ("16_Rychlosti.txt", "r", encoding = "UTF-8") as subor:
    data =  subor.readlines()
    
pocet_zaznam = len(data)
print(pocet_zaznam)

def spz():
    for i in data:
        zoznam.append(i.strip().split())
    
    max_speed = zoznam[0][3]
    for i in range (len(zoznam)):
        docasna_speed = zoznam[i][3]
        if  int(docasna_speed) > int(max_speed):
            max_speed = docasna_speed
            najrych_spz = zoznam[i][2]
            
    
    print("Najvačšia rychlosť je " + (max_speed) + " km/h" + "a jeho spz je " + (najrych_spz))

spz()