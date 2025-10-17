# összegzés algoritmusa

lista = [54, 12, 69, 87, 8]

összeg = 0
for x in lista:
    összeg = összeg + x

print(f"A lista összuege: {összeg}")

#szétválogatás

tizenegy = []

for x in lista:
    if x % 11 == 0:
        tizenegy.append(x)

#Átlagszámítás
#legegyszerübb megoldas
jegyek = []
"""
for x in range(5):
    jegyek.append(int(input("Add meg a jegyet: ")))

    print(f"Jegyek: {jegyek}")

    print(f"Az átlag: {sum(jegyek)/len(lista)}")
"""
"""
for x in range(5):
    jegy = int(input("Adjon meg egy jegyet! >>> "))
    if jegy < 1:
        print(f"Adjon meg nagyobb számot!")
    elif jegy >5:
        print(f"Adjon meg egy kisebb számot!")
    else:
        jegyek.append(jegy)
"""
jegy = int(input("Adjon meg egy jegyet! >>> "))

while jegy != 0:
    jegy = int(input("Adjon meg egy jegyet! >>> "))
    if jegy < 1:
        print(f"Adjon meg nagyobb számot!")
    elif jegy > 5:
        print(f"Adjon meg egy kisebb számot!")
    else:
        jegyek.append(jegy)

átlag = sum(jegyek)/len(jegyek)
print(f"Az átlag: {átlag}")

if 1 < átlag and 2 > átlag:
    print("BUkás!")
elif 2 >= átlag and 2.6>=átlag:
    print("Elégséges!")