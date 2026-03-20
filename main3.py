from osztalyok3 import Film

filmek = []

with open("mozifilmek.csv", "r", encoding="utf-8") as importájl:
    next(importájl)
    for sor in importájl:
        adat = sor.strip().split(",")
        id = adat[0]
        title = adat[1]
        year = adat[2]
        genre = adat[3]
        director = adat[4]
        country = adat[5]
        language = adat[6]
        duration_min = adat[7]
        rating = adat[8]
        boxoffice_musd = adat[9]

        film = Film(id, title, year, genre, director, country, language, duration_min, rating, boxoffice_musd)
        filmek.append(film)

print(filmek[0])
