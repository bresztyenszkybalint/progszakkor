class Film:
    def __init__(self, id, title, year, genre, director, country, language, duration_min, rating, boxoffice_musd):
        self.id = int(id)
        self.title = str(title)
        self.year = int(year)
        self.genre = str(genre)
        self.director = str(director)
        self.country = str(country)
        self.language = str(language)
        self.duration_min = int(duration_min)
        self.rating = float(rating)
        self.boxoffice_musd = float(boxoffice_musd)

    def __str__(self):
        return f"{self.id}. {self.title}\n\tKiadás éve: {self.year}\n\tűfaj: {self.genre}\n\tSzinész: {self.director}\n\tOrszág: {self.country}\n\tNyelv: {self.language}\n\tHossz: {self.duration_min}\n\tIMBD értékelés:{self.rating}\n\tBevétel: {self.boxoffice_musd}"
