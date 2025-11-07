import random
szöveglista = []

for x in range (2500):
    sorsolt = random.randint(0, 1)
    if sorsolt == 0:
        szöveglista.append("a")
    else:
        szöveglista.append("b")

print(szöveglista)


db = 0
for i in range(len(szöveglista) - 3):
    if szöveglista[i] == "a" and szöveglista[i + 1] == "b" and szöveglista[i + 2] and szöveglista[i + 3]:
        db += 1

print(f"Az abba ennyiszer szerepel: {db}")