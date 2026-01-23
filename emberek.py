class Ember:
    def __init__(self, nev, eletkor, varos, magassag, suly, foglalkozas):
        self.nev = nev
        self.eletkor = eletkor
        self.varos = varos
        self.magassag = magassag
        self.suly = suly
        self.foglalkozas = foglalkozas

    def bemutatkozas(self):
        print(f"Szia! A nevem {self.nev}, {self.eletkor} éves vagyok, "
            f"{self.varos} városban élek, és a {self.foglalkozas} vagyok és a súlyom: {self.suly}.")

    def szülinap(self):
        self.eletkor += 1

    def koltozik(self, uj_varos):
        regi_varos = self.varos
        self.varos = uj_varos

    def testtomeg_index(self):
        magassag_meter = self.magassag/100
        bmi = self.suly/(magassag_meter ** 2)
        return round(bmi, 2)

    def hizas(self, kg):
        self.suly += kg

ember1 = Ember("Kiss Anna", 28, "Pécs", 168, 62, "programozó")
ember1.bemutatkozas()
ember1.szülinap()
ember1.koltozik("Kecskemét")
ember1.hizas(3)
ember1.bemutatkozas()
print(f"{ember1.testtomeg_index()}")

# ember2 = Ember("Szabó András", 72, "Szeged",  179, 50, "pék")
# ember2.bemutatkozas()

