import tkinter, random
canvas = tkinter.Canvas(width = 500, height= 300, bg = "dodgerblue")
canvas.pack()

def vajicko(x, y):
    canvas.create_oval(x-4, y-6, x+4, y+6, fill = "white")
    
def kosik(x):
    canvas.create_line(x, 285, x+50, 285, width = 10, fill = "brown")
    
def kosik_vlavo(udaje):
    global kosik_x
    kosik_x -= 5
    
def kosik_vpravo(udaje):
    global kosik_x
    kosik_x += 5
    
def skore(body):
    global hra_bezi
    canvas.create_text(250, 150, text = (f"Skóre : {body}"))
    hra_bezi = False
    


vajicko_x = random.randint(10, 490)
vajicko_y = 20
hra_bezi = True
kosik_x = 230
pocet_bodov = 0
pocet_vajec = 0

canvas.bind_all("<Left>", kosik_vlavo)
canvas.bind_all("<Right>", kosik_vpravo)


while hra_bezi:
    canvas.delete("all")
    vajicko(vajicko_x, vajicko_y)
    kosik(kosik_x)
    vajicko_y += 5
    if vajicko_y > 280:
        vajicko_y = 20
        vajicko_x = random.randint(10, 490)
        pocet_vajec += 1
        
    if 270 < vajicko_y < 280 and kosik_x < vajicko_x < kosik_x+50:
        pocet_bodov += 1
        print(pocet_bodov)
        
    if pocet_vajec == 3:
        skore(pocet_bodov)
        
    canvas.update()
    canvas.after(33)

canvas.mainloop()