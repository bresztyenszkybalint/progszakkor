class Termék:
    def __init__(self, név, kategória, ár):
        self.név = név
        self.kategória = kategória
        self.ár = ár
        self.kg = 1.0

    def infó(self):
        return f"{self.név}, {self.kategória} kategóriájú termék és az ára: {self.ár}, súlya: {self.kg} kg."

termék1 = Termék("Alma", "gyümölcs", 600)
termék2 = Termék("Retek", "zöldség", 700)

print(termék1.infó())
print(termék2.infó())

termék1.ár = 700

print(termék1.infó())