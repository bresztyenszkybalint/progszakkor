import random
számlista = []
kerekített_lista = []

for x in range(200):
    számlista.append(round(random.random())) # 0 és 1 között random szampokat general, de sose eri el a 0 at se es az 1 et se

print(számlista)

db = 0
for i in range(len(számlista) - 2):
    if számlista[i] == 1 and számlista[i + 1] == 0 and számlista[i + 2] ==1:
        db += 1

print(f"A 111 ennyiszer szerepel a listában: {db}")