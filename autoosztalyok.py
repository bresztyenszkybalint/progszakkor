class Auto:
    def __init__(self, markanev, modell, gyartasi_ev):
        self.markanev = markanev
        self.modell = modell
        self.gyartasi_ev = gyartasi_ev
        self.sebesseg = 0
        self.motor_bekapcsolva = False
        self.uzemanyag_szint =50.0
        self.kilometer_ora = 0

    def kiir_auto_adatok(self):
        return(f"Márka: {self.markanev}, Modell: {self.modell}, Gyártáso év: {self.gyartasi_ev},"
                f"Sebesség: {self.sebesseg} km/h, Motor állapot: "Bekapcsolva" if {self.motor_bekapcsolva} else "kikapcsolva""
                f"Üzemanyag szint: {self.uzemanyag_szint} liter, Kilométeróra {self.kilometer_ora} km.")
    
    def motor_indit(self):
        if not self.motor_bekapcsolva and self.uzemanyag_szint > 0:
            self.motor_bekapcsolva = True
            return "A motor beindult."
        elif self.uzemanyag_szint <= 0:
            return "Nincsen elég üzemanyag a beindításhoz."
        return "A motor már be van indítva"
    
    def motor_leallit(self):
        if self.motor_bekapcsolva:
            self.motor_bekapcsolva:
            self.motor_bekapcsolva = False
            self.sebesseg = 0
            return "A motor leállt."
        return "A motor le van állítva."
    
    def gyorsit(self, novekedes):
        if self.motor_bekapcsolva:
            self.sebesseg += novekedes
            return f"Gyorsítás: autó sebessége most {self.sebesseg} km/h."
        return "Nem lehet fékezni vagy az autó áll."
    
    def fekez(self, csokkenes):
        if self.motor_bekapcsolva and self.sebesseg > 0:
            self.sebesseg = max(0, self.sebesseg - csokkenes)
            return f"Fékezés: az autó sebessége most {self.sebesseg} km/h."

    def tankol(self, mennyiseg):
        self.uzemanyag_szint += mennyiseg
        return f"{mennyiseg} liter üzemanyag hozzáadva. Üzemanyagszint = {self.uzemanyag_szint} liter."
    
    def fogyaszt(self, kilometer):
        fogyasztas = kilometer * 0.1
        self.uzemanyag_szint -= fogyasztas
        if self.uzemanyag_szint < 0:
            self.uzemanyag_szint = 0
            self.kilometer_ora += kilometer
        uzenet = f"Megtett távolság: {kilometer} km, fogyasztott üzemanyag: {fogyasztas} liter."
        if self.uzemanyag_szint == 0:
            uzenet += "Elfogyott az üzemanyag!"
            self.motor_leallit()
        return uzenet
    
#1 Autó létrehozása
auto1 = Auto("Toyota", "Corolla", 2018)
auto2 = Auto("BMW", "320d", 2020)

# 2) Kiinduló adatok
print("Kezdő állapot (auto1):")
print(auto1.kiir_auto_adatok())
print()

# 3) Próbáljunk gyorsítani motor nélkül
print("Gyorsítás motor nélkül:")
print(auto1.gyorsit(20))
print()

# 4) Motor indítás
print("Motor indítás:")
print(auto1.motor_indit())
print()

# 5) Gyorsítás + fékezés
print(auto1.gyorsit(30))
print(auto1.gyorsit(15))
print(auto1.fekez(20))
print()

# 6) “Utazás” (üzemanyag fogyasztás)
print("Utazás 100 km:")
print(auto1.fogyaszt(100))
print("Állapot utána:")
print(auto1.kiir_auto_adatok())
print()

# 7) Tankolás
print("Tankolás 20 liter:")
print(auto1.tankol(20))
print(auto1.kiir_auto_adatok())
print()

# 8) Menjünk addig, amíg elfogy az üzemanyag
print("Menjünk 600 km-t (hogy biztos kifogyjon):")
print(auto1.fogyaszt(600))
print("Állapot a végén:")
print(auto1.kiir_auto_adatok())
print()

# 9) Másik autó gyors teszt
print("auto2 motor indítás + gyorsítás:")
print(auto2.motor_indit())
print(auto2.gyorsit(50))
print(auto2.fogyaszt(50))
print(auto2.motor_leallit())
print(auto2.kiir_auto_adatok())