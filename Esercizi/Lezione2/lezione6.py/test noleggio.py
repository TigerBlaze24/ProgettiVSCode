import unittest
from contextlib import redirect_stdout  
from io import StringIO 
from film import Film,Azione,Commedia,Drama 
from esercizio noleggio import  test noleggio
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