import tkinter
import random

canvas = tkinter.Canvas(height = 400,width = 400)
canvas.pack()

zoznam = []
farby = ["green", "blue", "red", "pink", "yellow", "orange", "brown", "sky blue", "magenta", "cyan"]


for i in range(10):
    canvas.delete("all")
    zoznam.append(random.randint(0, 20))
    canvas.create_text(200, 200, text = zoznam[i], font = ("ARIAL", 250), fill=farby[i])
    canvas.after(500)
    canvas.update()
     
    
nove_cislo = random.randint(0, 20)

print(nove_cislo)
odpoved = input("Bolo tam toto číslo ? ")


if odpoved == "A" and nove_cislo in zoznam:
    print("Mas pravdu")
    
elif odpoved == "A" and nove_cislo not in zoznam:
    print("Nemas pravdu")
    
elif odpoved == "N" and nove_cislo in zoznam:
    print("Nemas pravdu")
    
else:
    print("Mas pravdu")

###Overiť ked napíše nezmysel