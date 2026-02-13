with open("./doga.txt", "r", encoding="utf-8") as célfájl:
    szoveg = célfájl.read()

print(f"Karakterek szama: {len(szoveg)}")

#karakterek_szama = len(szoveg)
sorok_szama = len(szoveg.split("\n"))

piramidusdb = szoveg.lower().split().count("piramis")

#2

szoveg = szoveg.lower()

karakterek = [".", ",", ":", ";", "?", "!", "'", '"', "-", "_", "  ", "(", ")"]

for jel in karakterek:
    szoveg = szoveg.replace(jel, " ")

szavak = szoveg.split()

tisztitott = []

for szo in szavak:
    if szo != "":
        tisztitott.append(szo)

print(tisztitott)

with open("clean.txt", "w", encoding="utf-8") as célclean:
    print(*tisztitott, file=célclean)

#3
print(f"lista hossza: {len(szavak)}")
print(f"Elso 10 szo {szavak[:10]}")
print(f"Utolso 10 szo {szavak[-10:]}")

#4
rovid_szavak = []
hosszu_szavak = []

for szo in szavak:
    if len(szo) < 4:
        rovid_szavak.append(szo)
    
for szo in szavak:
    if len(szo) > 10:
        hosszu_szavak.append(szo)

#



