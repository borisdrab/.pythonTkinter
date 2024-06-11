##Not finished

import tkinter
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

def zastav():
    global bezi
    bezi = False
    
    
def resetuj():
    canvas.delete("all")
    
    
def start():
    global bezi
    bezi = True 

bezi = True
pocitadlo = 0

stopka = tkinter.Button(text = ("Stop"), command = zastav)
stopka.pack()

reset = tkinter.Button(text = ("Reset"), command = resetuj)
reset.pack()

start = tkinter.Button(text = ("Start"), command = start)
start.pack()


while bezi:
    canvas.delete("all")
    pocitadlo += 1
    canvas.create_text(200,200, text = round(pocitadlo*0.01, 2), font = ("ARIAL", 35))
    canvas.after(10)
    canvas.update()

canvas.mainloop()


########################################################################################################################################################################
def stop():
    global cas
    cas = False

def stopky():
    global cas
    cas = True
    sek = 0
    while cas == True:
        canvas.delete('all')
        canvas.create_text(250,250, text= round(sek, 2), font=('Arial', 20))
        sek += 0.1
        canvas.update()
        canvas.after(50)

start = tkinter.Button(text='Start', command=stopky)
start.pack()
koniec = tkinter.Button(text='Stop', command=stop)
koniec.pack()
