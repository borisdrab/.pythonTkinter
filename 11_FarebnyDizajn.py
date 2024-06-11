import tkinter
import random

canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

n = int(input("Zadaj počet štvorcov: "))

farba = ["green", "red", "blue", "yellow", "cyan", "brown", "purple", "pink", "black", "grey"]

x, y = 125, 100

def kolonka():
    canvas.create_rectangle(x, y, x+150, y+150)

kolonka()

def pattern():
    z = 150/n
    fareb_index = 0
    for j in range (n):
        for i in range(n):
            akt_farba = farba[fareb_index]
            canvas.create_rectangle(x+(z*i), y+(z*j), x+(z*(i+1)), y+(z*(j+1)), fill = akt_farba) 
            fareb_index = (fareb_index + 1) % len(farba)


pattern()

canvas.mainloop()