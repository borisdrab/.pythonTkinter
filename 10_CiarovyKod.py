from cgitb import text
import random
import tkinter

canvas = tkinter.Canvas(height = 400, width = 400)
canvas.pack()

a = 150
b = 100
c = 150

cislo = random.randint(0, 9)
canvas.create_line(150, 100, 150, 200, width =cislo)
canvas.create_text(160, 190, text =cislo)

for i in range(6):
    cislo1 = random.randint(0, 9)
    a += 10
    canvas.create_line(a, b, a, b+80, width = cislo1)
    canvas.create_text(c+18, b+90, text = cislo1)
    c += 8

cislo2 = random.randint(0, 9)
canvas.create_line(224, 100, 224, 200, width = cislo2)
canvas.create_text(216, 190, text =cislo2)

canvas.mainloop()