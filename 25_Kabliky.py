#Not Finished

import tkinter, random
canvas = tkinter.Canvas(width=420, height=150, bg='white')
canvas.pack()

farby = ['green', 'red', 'grey', 'blue', 'orange', 'cyan', 'brown', 'black']
x, y, dlzka = 50, 50, 100
cas = 60
uhadol = False
spravny = random.randrange(len(farby))

def vykresli():
    for i in range(len(farby)):
        canvas.create_rectangle(x, y+i*10, x+dlzka, y+i*10+10, fill=farby[i])

def klik(sur):
    global uhadol
    if 50< sur.x <150 and cas > 0:
        poradie = (sur.y - y) // 10
        if  0 <= poradie < len(farby) :
            print(poradie)
            if poradie == spravny:
                uhadol = True
                canvas.create_text(200, 130, text='Vyhral si!', fill="green", font='Arial 30')
            else:
                canvas.create_text(200, 130, text='Prehral si!', fill = "red", font='Arial 30')
def animacia():
    global cas
    cas -= 1
    canvas.delete('cas')
    canvas.create_text(300, 75, text=cas, font='Arial 30', fill='red',tags='cas')
    if cas>0 and not uhadol:  
        canvas.after(100, animacia)
    elif not uhadol:
        canvas.delete('all')
        canvas.create_text(200, 130, text='Prehral si!', fill = "red", font='Arial 30')
    
 

vykresli()
canvas.bind('<Button-1>', klik)
animacia()
canvas.mainloop()