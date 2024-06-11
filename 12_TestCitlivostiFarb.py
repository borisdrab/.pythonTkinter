import tkinter
import random
canvas = tkinter.Canvas(width = 1000, height = 1000)
canvas.pack()

x = 50
y = 50
pocitadlo = 1

r = random.randint(0, 255)
r2 = random.randint(0, 255)
g = 0
b = 0
nahodny_index = 0


farba = f"#{r:02X}{g:02X}{b:02x}"
farba2 = f"#{r2:02x}{g:02x}{b:02x}"

def vsetky():
    global pocitadlo
    global x
    for i in range (25):
        canvas.create_rectangle(x, y, x+25, y+25, fill = farba)
        canvas.create_text(x+12.5, 85, text = pocitadlo )
        x += 25
        pocitadlo += 1
    x = 50
    
vsetky()
 

def jeden():
    global nahodny_index
    nahodny_index = random.randint(1, 25)
    canvas.create_rectangle(x+(nahodny_index*25), y, x+25+(nahodny_index*25), y+25, fill = farba2)
    nahodny_index += 1
    
    print(nahodny_index)
    
jeden()

oznac = int(input("Vyber štvorec s inou farbou : "))

def overenie():
    if oznac == nahodny_index:
        print("Správne")
    else:
        print("Zle")

overenie()

canvas.mainloop()