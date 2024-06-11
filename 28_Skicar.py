import tkinter 
import random 
canvas = tkinter.Canvas(height = 400, width = 400)
canvas.pack()

f = " "
hr = 10



farby = ["red", "green", "blue", "black", "pink"]

def kreslenie(event):
    x = event.x
    y = event.y
    canvas.create_oval(x, y, x+hr, y-hr, fill = f, width = 0)


def tabulky():
    global a,b
    a = 25
    b = 25
    for i in range (5):
        canvas.create_rectangle(a+(i*50), b, a+(i*50)+50, b+50, fill = farby[i-1])
    canvas.create_text(a+300, b+35, text = "Vymazať")


def klik(udaje):
    global f
    global hr 

    klik_x = udaje.x
    klik_y = udaje.y
    if klik_x >= a + 25 and klik_x <= a + 75 and klik_y>= b:
        f="pink"
    if klik_x >= a + 75 and klik_x <= a + 125 and klik_y>= b :
        f = "red"
    if klik_x >= a + 125 and klik_x <= a + 175 and klik_y>= b :
        f = "green"
    if klik_x >= a + 175 and klik_x <= a + 225 and klik_y>= b :
        f = "blue"
    if klik_x >= a + 225 and klik_x <= a + 270 and klik_y>= b :
        f = "black"
    


canvas.bind("<B1-Motion>", kreslenie)
canvas.bind("<Button-1>", klik)
tabulky()

canvas.mainloop()