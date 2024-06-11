import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()
import random
x=220
guess = input('zadaj 5 čísel: ')
haha = []
for i in guess:
    haha.append(i)
print(haha)

ruleta = str(random.randint(10000,99999))
print(ruleta)
hehe=[]
for j in guess:
    hehe.append(i)
canvas.create_text(250,300,text=guess)
canvas.create_text(250,200,text=ruleta)

for k in range(len(ruleta)):
    if ruleta[k] == guess[k]:
        canvas.create_oval(x,245,x+10,255,fill='green')
    else:
        canvas.create_oval(x,245,x+10,255,fill='red')
    x+=15
        

canvas.mainloop()