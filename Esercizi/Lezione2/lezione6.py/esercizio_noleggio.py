class Film:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def setID(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def getID(self):
        return self.id

    def getTitle(self):
        return self.title

    def isEqual(self, otherFilm):
        return self.id == otherFilm.getID()


class Azione(Film):
    def __init__(self, id, title):
        super().init(id, title)
        self.genere = "Azione"
        self.penale = 3.0

    def getGenere(self):
        return self.genere

    def getPenale(self):
        return self.penale

    def calcolaPenaleRitardo(self, days):
        return self.penale * days


class Commedia(Film):
    def __init__(self, id, title):
        super().init(id, title)
        self.genere = "Commedia"
        self.penale = 2.5

    def getGenere(self):
        return self.genere

    def getPenale(self):
        return self.penale

    def calcolaPenaleRitardo(self, days):
        return self.penale * days


class Drama(Film):
    def __init__(self, id, title):
        super().init(id, title)
        self.genere = "Drama"
        self.penale = 2.0

    def getGenere(self):
        return self.genere

    def getPenale(self):
        return self.penale

    def calcolaPenaleRitardo(self, days):
        return self.penale * days


class Noleggio:
    def __init__(self, film_list):
        self.film_list = film_list
        self.rented_film = {}

    def isAvailable(self, film):
        for available_film in self.film_list:
            if film.isEqual(available_film):
                print(f"Il film scelto è disponibile: {film.getTitle()}!")
                return True
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")
        return False

    def rentAMovie(self, film, clientID):
        if self.isAvailable(film):
            self.film_list.remove(film)
            if clientID in self.rented_film:
                self.rented_film[clientID].append(film)
            else:
                self.rented_film[clientID] = [film]
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")

    def giveBack(self, film, clientID, days):
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            penalty = film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penalty} euro!")
        else:
            print(f"Il cliente {clientID} non ha noleggiato il film {film.getTitle()}!")

    def printMovies(self):
        for film in self.film_list:
            genre = ""
            if isinstance(film, Azione):
                genre = "Azione"
            elif isinstance(film, Commedia):
                genre = "Commedia"
            elif isinstance(film, Drama):
                genre = "Drama"
            print(f"{film.getTitle()} - {genre} -")
def printRentMovies(self, clientID):
        if clientID in self.rented_film:
            print(f"Film noleggiati dal cliente {clientID}:")
            for film in self.rented_film[clientID]:
                genre = ""
                if isinstance(film, Azione):
                    genre = "Azione"
                elif isinstance(film, Commedia):
                    genre = "Commedia"
                elif isinstance(film, Drama):
                    genre = "Drama"
                print(f"{film.getTitle()} - {genre} -")
        else:
            print(f"Il cliente {clientID} non ha noleggiato alcun film.")
