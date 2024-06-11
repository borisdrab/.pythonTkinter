import tkinter
import random


canvas = tkinter.Canvas(height = 400, width=400)
canvas.pack()
skore = 0

fx = 0
fy = 0

def stvorec():
    canvas.delete("all")
    global suradnica_x, suradnica_y
    suradnica_x = random.randint(10, 390)
    suradnica_y = random.randint(10, 390)
    canvas.create_rectangle(suradnica_x, suradnica_y, suradnica_x+30, suradnica_y+50, fill = "cyan")
    canvas.create_text(340, 20, text = f"Počet skóre: {skore}") 
    canvas.after(1000, stvorec)


stvorec()

def click(data):
    global skore, fx, fy
    fx = data.x
    fy = data.y
    if suradnica_x < fx < suradnica_x+30 and suradnica_y < fy < suradnica_y + 50 :
        skore += 1
    else:
        skore -= 1

canvas.bind("<Button-1>", click)
canvas.mainloop()