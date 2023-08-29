dvd_collections = [None] * 15

class DVD:
    def __init__(self, name, release_year, director):
        self.name = name
        self.release_year = release_year
        self.director = director
    
    def __str__(self):
        return f"{self.name}, directed by {self.director}, released in {self.release_year}"

dvd_collections[0] = DVD("Movie 1", 2000, "Director 1")
dvd_collections[1] = DVD("Movie 2", 2005, "Director 2")

for dvd in dvd_collections:
    if dvd:
        print(dvd)
