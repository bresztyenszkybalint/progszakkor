# ====== FÁJLNEVEK ======
bemeneti_fajl = "forrás.txt"
tisztitott_fajl = "clean.txt"
top10_fajl = "top10.csv"
evszamok_fajl = "evszamok.txt"
riport_fajl = "riport.txt"


# ====== 1. BEOLVASÁS ======
fajl = open(bemeneti_fajl, "r", encoding="utf-8")
szoveg = fajl.read()
fajl.close()

karakterek_szama = len(szoveg)
sorok_szama = len(szoveg.split("\n"))

# "rock" szó számolása (kis/nagybetű független)
rock_db = szoveg.lower().split().count("rock")

print("1. Alapstatisztika")
print("Karakterek száma:", karakterek_szama)
print("Sorok száma:", sorok_szama)
print('"rock" szó előfordulás:', rock_db)
print()


# ====== 2. SZÖVEGTISZTÍTÁS ======
kisbetus_szoveg = szoveg.lower()

# Írásjelek eltávolítása
irasjelek = ".,!?;:\"'()-[]{}_/\\"
tisztitott_szoveg = ""

for karakter in kisbetus_szoveg:
    if karakter not in irasjelek:
        tisztitott_szoveg += karakter

# dupla szóközök eltávolítása
while "  " in tisztitott_szoveg:
    tisztitott_szoveg = tisztitott_szoveg.replace("  ", " ")

tisztitott_szoveg = tisztitott_szoveg.strip()

fajl = open(tisztitott_fajl, "w", encoding="utf-8")
fajl.write(tisztitott_szoveg)
fajl.close()

print("2. Tisztított szöveg mentve:", tisztitott_fajl)
print()


# ====== 3. SZAVAK LISTÁJA ======
szavak = tisztitott_szoveg.split()

print("3. Szavak listája")
print("Szavak száma:", len(szavak))
print("Első 10 szó:", szavak[:10])
print("Utolsó 10 szó:", szavak[-10:])
print()


# ====== 4. RÖVID ÉS HOSSZÚ SZAVAK ======
rovid_szavak = []
hosszu_szavak = []

for szo in szavak:
    if len(szo) < 4:
        rovid_szavak.append(szo)
    if len(szo) > 10:
        hosszu_szavak.append(szo)

print("4. Szűrés")
print("4 karakternél rövidebb szavak száma:", len(rovid_szavak))
print("10 karakternél hosszabb szavak száma:", len(hosszu_szavak))
print()


# ====== 5. DUPLIKÁTUMOK ELTÁVOLÍTÁSA ======
egyedi_szavak = []

for szo in szavak:
    if szo not in egyedi_szavak:
        egyedi_szavak.append(szo)

egyedi_szavak.sort()

print("5. Egyedi szavak száma:", len(egyedi_szavak))
print("ABC sorrendben az egyedi szavak:")
print(egyedi_szavak)
print()


# ====== 6. RENDEZÉS HOSSZ SZERINT ======
szavak_hossz_szerint = sorted(szavak, key=len, reverse=True)

print("6. 5 leghosszabb szó:")
print(szavak_hossz_szerint[:5])
print()


# ====== 7. GYAKORISÁGI STATISZTIKA ======
gyakorisag = {}

for szo in szavak:
    if szo in gyakorisag:
        gyakorisag[szo] += 1
    else:
        gyakorisag[szo] = 1

# rendezés gyakoriság szerint
rendezett = sorted(gyakorisag.items(), key=lambda elem: elem[1], reverse=True)

print("7. 10 leggyakoribb szó:")
for szo, db in rendezett[:10]:
    print(szo, "->", db)

# CSV mentés
fajl = open(top10_fajl, "w", encoding="utf-8")
fajl.write("szo,db\n")
for szo, db in rendezett[:10]:
    fajl.write(szo + "," + str(db) + "\n")
fajl.close()

print("Mentve:", top10_fajl)
print()


# ====== 8. ÉVSZÁMOK KIGYŰJTÉSE ======
evszamok = []

for szo in szoveg.split():
    if len(szo) == 4 and szo.isdigit():
        if int(szo) not in evszamok:
            evszamok.append(int(szo))

evszamok.sort()

fajl = open(evszamok_fajl, "w", encoding="utf-8")
for ev in evszamok:
    fajl.write(str(ev) + "\n")
fajl.close()

print("8. Talált évszámok:")
print(evszamok)
print("Mentve:", evszamok_fajl)
print()


# ====== 9. MONDATOK KEZELÉSE ======
mondatok = []
aktualis_mondat = ""

for karakter in szoveg:
    aktualis_mondat += karakter
    if karakter in ".!?":
        mondatok.append(aktualis_mondat.strip())
        aktualis_mondat = ""

# rendezés hossz szerint
mondatok_hossz_szerint = sorted(mondatok, key=len)

legrovidebb_mondatok = mondatok_hossz_szerint[:3]
leghosszabb_mondatok = mondatok_hossz_szerint[-3:]

print("9. 3 leghosszabb mondat:")
for m in leghosszabb_mondatok:
    print("-", m)

print("\n3 legrövidebb mondat:")
for m in legrovidebb_mondatok:
    print("-", m)
print()


# ====== 10. RIPORT KÉSZÍTÉSE ======
fajl = open(riport_fajl, "w", encoding="utf-8")

fajl.write("RIPORT\n")
fajl.write("====================\n")
fajl.write("Karakterek száma: " + str(karakterek_szama) + "\n")
fajl.write("Szavak száma: " + str(len(szavak)) + "\n")
fajl.write("Egyedi szavak száma: " + str(len(egyedi_szavak)) + "\n")
fajl.write("\nTop 5 leggyakoribb szó:\n")

for szo, db in rendezett[:5]:
    fajl.write(szo + " -> " + str(db) + "\n")

fajl.write("\nTalált évszámok:\n")
for ev in evszamok:
    fajl.write(str(ev) + "\n")

fajl.close()

print("10. Riport mentve:", riport_fajl)
