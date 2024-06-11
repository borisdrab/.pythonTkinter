#NotFinished

udaje = []

with open ("17_signup.txt", "r", encoding = "UTF-8") as subor:
    data = subor.readlines()
    for i in data:
        udaje.append(i.strip().split())
        
meno = input("Zadaj prihlasovacie meno: ")

for z in range(len(udaje)):
    if meno in udaje:
        heslo = input("Zadaj prihlasovacie heslo: ")
        if heslo == udaje[z][1]:
            print("Správne!")
        else:
            print("Nesprávne zadané heslo!")
    else:
        print("Nevhodne zadané meno!")
        break
        

