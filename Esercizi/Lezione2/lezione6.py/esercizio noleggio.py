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


class TestFilm(unittest.TestCase):
    def setUp(self):
        # Creazione di una lista di film per il test
        self.film_list = [
            Azione(1, "Film Azione 1"),
            Azione(2, "Film Azione 2"),
            Azione(3, "Film Azione 3"),
            Azione(4, "Film Azione 4"),
            Azione(5, "Film Azione 5"),
            Commedia(6, "Film Commedia 1"),
            Commedia(7, "Film Commedia 2"),
            Commedia(8, "Film Commedia 3"),
            Commedia(9, "Film Commedia 4"),
            Drama(10, "Film Drama 1")
        ]
        # Inizializzazione dell'oggetto Noleggio
        self.video_store = Noleggio(self.film_list)

    def test_isAvailable(self):
        self.assertTrue(self.video_store.isAvailable(self.film_list[0]))
        fake_film = Film(100, "Film Fittizio")
        self.assertFalse(self.video_store.isAvailable(fake_film))

    def test_rentAMovie(self):
        clientID = 1
        film_to_rent = self.film_list[0]
        self.video_store.rentAMovie(film_to_rent, clientID)
        self.assertNotIn(film_to_rent, self.video_store.film_list)
        self.assertIn(film_to_rent, self.video_store.rented_film[clientID])

    def test_rentAMovie_notAvailable(self):
        clientID = 1
        film_to_rent = Film(100, "Film Non Disponibile")
        self.video_store.rentAMovie(film_to_rent, clientID)
        self.assertNotIn(film_to_rent, self.video_store.rented_film.get(clientID, []))

    def test_giveBack(self):
        clientID = 1
        film_to_rent = self.film_list[0]
        self.video_store.rentAMovie(film_to_rent, clientID)
        self.video_store.giveBack(film_to_rent, clientID, 5)
        self.assertIn(film_to_rent, self.video_store.film_list)
        self.assertNotIn(film_to_rent, self.video_store.rented_film[clientID])
def testcalcolaPenaleRitardo(self):
        film = Azione(1, "Film Azione")
        self.assertEqual(film.calcolaPenaleRitardo(3), 9.0)
        film = Commedia(2, "Film Commedia")
        self.assertEqual(film.calcolaPenaleRitardo(4), 10.0)
        film = Drama(3, "Film Drama")
        self.assertEqual(film.calcolaPenaleRitardo(2), 4.0)

    def testprintMovies(self):
        expectedoutput = [
            "Film Azione 1 - Azione -",
            "Film Azione 2 - Azione -",
            "Film Azione 3 - Azione -",
            "Film Azione 4 - Azione -",
            "Film Azione 5 - Azione -",
            "Film Commedia 1 - Commedia -",
            "Film Commedia 2 - Commedia -",
            "Film Commedia 3 - Commedia -",
            "Film Commedia 4 - Commedia -",
            "Film Drama 1 - Drama -"
        ]

        with StringIO() as buffer, redirectstdout(buffer):
            self.video_store.printMovies()
            output = buffer.getvalue().strip().split('\n')

        self.assertListEqual(output, expected_output)

    def test_printRentMovies(self):
        clientID = 1
        film_to_rent = self.film_list[0]
        self.video_store.rentAMovie(film_to_rent, clientID)

        expected_output = [
            f"Film noleggiati dal cliente {clientID}:",
            f"{film_to_rent.getTitle()} - {film_to_rent.getGenere()} -"
        ]

        with StringIO() as buffer, redirect_stdout(buffer):
            self.video_store.printRentMovies(clientID)
            output = buffer.getvalue().strip().split('\n')

        self.assertListEqual(output, expected_output)


if __name == '__main':
    unittest.main()
Questo è il terzo ed ultimo file del primo esercizio, "test_blockbuster.py", il file dei test in pratica
Esercizio n2
class DatabaseDate:
    def init(self):
        self.dates = {}  # Dizionario per memorizzare le date nel formato gg.mm.aaaa

    def aggiungi_data(self, data_str):
        """
        Aggiunge una nuova data al database.

        Args:
        

    data_str (str): Stringa rappresentante la data nel formato gg.mm.aaaa


        Raises:
        

    ValueError: Se la data è già presente nel database"""
          if data_str in self.dates:
              raise ValueError("Data già presente nel database")
          self.dates[data_str] = True


    def elimina_data(self, data_str):
        """
        Elimina una data dal database.

        Args:
        

    data_str (str): Stringa rappresentante la data nel formato gg.mm.aaaa


        Raises:
        

    ValueError: Se la data non è presente nel database"""
          if data_str not in self.dates:
              raise ValueError("Data non presente nel database")
          del self.dates[data_str]


    def modifica_data(self, data_str_vecchia, data_str_nuova):
        """
        Modifica una data nel database.

        Args:
        

    data_str_vecchia (str): Stringa rappresentante la data da modificare nel formato gg.mm.aaaa
        data_str_nuova (str): Nuova stringa rappresentante la data nel formato gg.mm.aaaa


        Raises:
        

    ValueError: Se la data da modificare non è presente nel database"""
          if data_str_vecchia not in self.dates:
              raise ValueError("Data da modificare non presente nel database")
          if data_str_nuova in self.dates:
              raise ValueError("Nuova data già presente nel database")
          self.elimina_data(data_str_vecchia)
          self.aggiungi_data(data_str_nuova)

def querydata(self, datastr):
        """
        Esegue una query nel database per ottenere una data specifica.

        Args:
        

    data_str (str): Stringa rappresentante la data da cercare nel formato gg.mm.aaaa


        Returns:
        

    str: La data richiesta se presente nel database


        Raises:
        

    ValueError: Se la data non è presente nel database"""
          if data_str not in self.dates:
              raise ValueError("Data non presente nel database")
          return data_str