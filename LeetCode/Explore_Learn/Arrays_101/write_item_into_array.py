class DVD:
    def __init__(self, name, release_year, director):
        self.name = name
        self.release_year = release_year
        self.director = director
    
    def __str__(self):
        return f"{self.name}, directed by {self.director}, released in {self.release_year}"

dvdCollections = [None] * 15
dvdCollections[7] = DVD("The Avengers", 2012, "Joss Whedon")
print(dvdCollections[7])
