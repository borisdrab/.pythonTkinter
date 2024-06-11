text = "Our online English classes feature lots of useful learning materials and activities to help you develop your reading skills with confidence in a safe"

znaky = [".", ",", "!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
for i in znaky:
    text = text.replace(i, "")
print(text)
text = text.upper()
abeceda = {}

for i in text:
    if i not in abeceda:
        abeceda[i] = 1
    else:
        abeceda[i] += 1

opak = 0
znak = ""
print(abeceda)
for i in abeceda:
    if abeceda[i] > opak:
        opak = abeceda[i]
        znak = i
print(f"{znak}:{opak}")