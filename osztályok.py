from datetime import date

class Ember:
    def __init__(self, nev, eletkor): # tulajdonságok, amiket megadhatok és dolgozhatok vele
        self.nev = nev # self az osztályon belüli műveletekhez
        self.eletkor = eletkor

    def koszones(self):
        return f"Szia, {self.nev} vagyok, {self.eletkor} éves."

    def szuletesi_ev(self):
        aktualis_ev = date.today().year
        return aktualis_ev - self.eletkor

    def egy_ev_mulva(self):
        return self.eletkor + 1

    def noveli_eletkort(self, ev):
        self.eletkor += ev

    def idosebb_e(self, masik_ember):
        if self.eletkor > masik_ember.eletkor:
            return f"{self.nev} idősebb, mint {masik_ember.nev}."
        elif self.eletkor < masik_ember.eletkor:
            return f"{masik_ember.nev} idősebb, mint {self.nev}."
        else:
            return "Egyidősek."

    def kategoria(self):
        if self.eletkor < 14:
            return "gyermek"
        elif self.eletkor < 65:
            return "felnőtt"
        else:
            return "idős"

    def hany_ev_mulva_lesz(self, cel_kor):
        if cel_kor <= self.eletkor:
            return 0
        return cel_kor - self.eletkor

    def forditott_nev(self):
        return " ".join(self.nev.split()[::-1])

    def eletkor_kulonbseg(self, masik_ember):
        return abs(self.eletkor - masik_ember.eletkor)

    def vegso_koszones(self):
        return f"Szia! {self.nev} vagyok, {self.eletkor} éves, és {self.kategoria()} kategóriába tartozom."
    

ember1 = Ember("Anna", 30)
print(ember1.koszones())
print(ember1.szuletesi_ev())
ember2 = Ember("Béla", 35)
print(ember2.koszones())
print(ember2.szuletesi_ev())
ember3 = Ember("Sándor", 40)
print(ember3.koszones())
print(ember3.szuletesi_ev())

print(ember1.koszones())
print("Anna születési éve:", ember1.szuletesi_ev())
print("Anna egy év múlva:", ember1.egy_ev_mulva(), "éves lesz.")

ember1.noveli_eletkort(5)
print("Anna életkora 5 év múlva:", ember1.eletkor)

print(ember1.idosebb_e(ember2))

print("Anna kategóriája:", ember1.kategoria())
print("Anna hány év múlva lesz 50 éves:", ember1.hany_ev_mulva_lesz(50))
print("Anna neve fordítva:", ember1.forditott_nev())
print("Anna és Béla életkor különbsége:", ember1.eletkor_kulonbseg(ember2))
print(ember1.vegso_koszones())
