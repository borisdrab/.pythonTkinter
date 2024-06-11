karta = "1236525256789"
sucet = 0
for cifra in karta [-2::-2]:
    medzisucet = 2*int(cifra)
    if medzisucet > 9:
        medzisucet = str(medzisucet)
        medzisucet = int(medzisucet[0]+medzisucet[1])
    sucet += medzisucet

for cifra in karta [-1::-2]:
    sucet += int(cifra)

print(sucet)
if sucet%10 == 0:
    print("Karta je platná.")
else:
    print("Karta nie je platná") 