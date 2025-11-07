# mintakeresés

import random
számlista = []
"""
for x in range(1000):
    számlista.append(random.randint(1, 10))

print(számlista)

db = 0
for x in range (len(számlista) - 2):
    if számlista[x] == 1 and számlista[x + 1] == 2 and számlista[x + 2] == 1:
        db += 1

print(f"A 721 ennyiszer szerepel: {db}")
"""




for x in range(2000):
    számlista.append(random.randint(1, 20))

print(számlista)

db = 0
for x in range (len(számlista) - 2):
    if számlista[x] == 11 and számlista[x + 1] == 5 and számlista[x + 2] == 3:
        db += 1

print(f"A 721 ennyiszer szerepel: {db}")