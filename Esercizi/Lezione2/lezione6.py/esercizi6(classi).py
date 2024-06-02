class Person:    
  def __init__(self, name, age):
       self.name = name
       self.age = age
alice = Person("Alice", 45)
bob = Person("Bob", 36)
print(bob.age)
Persone=[alice,bob, Person("Filippo",30),Person("Alina", 56),Person("Mike", 44)]
print(Persone)
min_age:int=float('inf')
index_min_age:int= 0
for i in range(len(Persone)):
   if Persone[i].age<min_age:
    min_age= Persone[i].age
    index_min_age = i
print( f'il nome della persona piu giovane{[index_min_age]}')
#facendo la funzione def__str__(self)->str:
#return f'Person(name={self.name})'
#si evita di printare tutte le classi ogni volta
class student:
  def __init__(self,name: str, studyprogram:str,age:str,gender:str):
       self.name = name
       self.studyrprgram = studyprogram
       self.age= age
       self.gender = gender
def __str__(self)->str:
         return f'student(name={self.name}, age ={self.age}, gender={self.gender})'
studenti =[ student("Filippo","medicina",18,"M"),student("Alina","matematica",20,"F"),student("Mike", "fisica",40,"M")]
io=student("Filippo","medicina",18,"M")
filippo=student("Alina","matematica",20,"F")
mike =student("Mike", "fisica",40,"M")
for studente in studenti:
    print(studente.name)
    print(studente.studyrprgram)
    print(studente.age)
    print(studente.gender)
#################################################################################################
class animal:
  def __init__(self,name: str, legs:int):
       self.name = name
       self.legs = legs
  def get_legs(self) -> int:
      return self.legs
cane = animal("cane",4)
print(cane.get_legs())

 ##########################################################################  
    
class food:
    def __init__(self,name: str, price:str,description:str):
        self.name = name
        self.price = price
        self.description= description
    def __str__(self)->str:
        return f'(name={self.name},price={self.price},description={self.description})'
piatti  =[food("lasagna",8,"pasta"),food("cannelloni",5,"pasta"),food("pollo alla diavola", 10,"pollo")]
class menu:
    foods=[]
    def addfood(self,food:list[food] =[]):
        self.foods.append(food)
    def __removefood__(self,food:list[food] =[]): 
        self.foods.append(food)
    def __str__(self)-> str:
        repr:str =""
        for food in self.foods:
            repr += food.__str__() +"\n"
        return repr[:-1]
cimbellone=food(name="ciambellone",price=10,description="dolce a forma di anello")
tiramisu=food(name="tiramisu",price=8,description="dolce al mascarpone e caffe")
budino=food(name="budino",price=5,description="dolce al cucchiaio")

menu = menu()
menu.addfood(cimbellone)
menu.addfood(tiramisu)
menu.addfood(budino)
print (menu)

   #1Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono sodd#
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    
    if conditionA or (conditionB and conditionC):
        return "Operazione permessa"
    else:
        return "Operazione negata"


print(check_combination(True, False, False))
print(check_combination(False, True, True))  
print(check_combination(False, False, True)) 

def remove_duplicates() -> list:
    unic = []
    for element in list:
        if element not in unic:
            unic.append(element)
    return unic


'''
esercio 2 Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
def rimuovi_elementi(lista, dizionario):
    for elemento, frequenza in dizionario.items():
        for _ in range(frequenza):
            if elemento in lista:
                lista.remove(elemento)
    return lista
'''

#esercizio 3 Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.#
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for chiave, valore in da_rimuovere.items():
        while valore in lista:  
            lista.remove(valore)
    return lista


lista_dati = [1, 2, 3,2,4]
dizionario_da_rimuovere = {2: 2, 4: 1}
nuova_lista = rimuovi_elementi(lista_dati, dizionario_da_rimuovere)

 #esercizio 4 ripassoScrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.#
def aggrega_voti(voti: dict) -> dict[str:list[int]]:
    
    aggrega_vot = {}
    
    for studente in voti:
        nome = studente["nome"]
        voto = studente['voto']
        if  nome in aggrega_vot:
            aggrega_vot[nome].append(voto)
        else:
            aggrega_vot[nome] = [voto]
    return aggrega_vot
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
#########################
#nuovi esercizi classi:
 
class Film:
    def __init__(self, titolo: str, durata: int):
        self.titolo = titolo
        self.durata = durata


class Sala:
    def __init__(self, filmprogrammazione: Film, postitotali: int, postiprenotati: int):
        self.filmprogrammazione = filmprogrammazione
        self.postitotali = postitotali
        self.postiprenotati = postiprenotati

    def prenota_posti(self, num_posti: int) -> str:
        postidisponibili: int = self.postitotali - self.postiprenotati
        if self.postiprenotati <= postidisponibili:
            self.postiprenotati += num_posti
            return "conferma" or "errore"

    def posti_disponibili(self) -> int:
        return self.postitotali - self.postiprenotati


class Cinema:
    def __init__(self):
        self.Sale = []

    def aggiungi_Sala(self, Sala):
        self.Sale.append(Sala)

    def prenota_film(self, titolo_film, num_posti):
        for i, Sala in enumerate(self.Sale):
            if Sala.filmprogrammazione.titolo == titolo_film:
                risultato_prenotazione = Sala.prenota_posti(num_posti)
                if risultato_prenotazione == "conferma":
                    return f"{titolo_film} Sala {i+1}"
                else:
                    return "Errore nella prenotazione."
        return "Film non trovato."

cinema = Cinema()
film1 = Film("Star Wars", 120)
Sala1 = Sala(film1, 50, 5)
cinema.aggiungi_Sala(Sala1)
print(cinema.prenota_film("Star Wars", 50))

#esercizio del magazzino:

class Prodotto:
    def __init__(self, nome: str, quantita: int):
        self.nome = nome
        self.quantita = quantita

class Magazzino:
    def __init__(self):
        self.prodotti = {}

    def aggiungi_prodotto(self, Prodotto):
        if Prodotto.nome in self.prodotti:
            self.prodotti[Prodotto.nome].quantita += Prodotto.quantita
        else:
            self.prodotti[Prodotto.nome] = Prodotto

    def cerca_prodotto(self, nome: str):
        if nome in self.prodotti:
            return self.prodotti[nome]
        else:
            return "Prodotto inesistente"

    def verifica_disponibilita(self, nome: str):
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            return f"Il prodotto è disponibile."
        else:
            return "Il prodotto non è disponibile"

magazzino = Magazzino()
prodotto1 = Prodotto("Caffé", 100)
prodotto2 = Prodotto("Zucchero", 50)
magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
print(magazzino.verifica_disponibilita("Caffé"))

#esercizioBiblioteca:

class Libro:
    def __init__(self, titolo: str, autore: str):
        self.titolo = titolo
        self.autore = autore
        self.prestito = "Non prestato"

    def presta(self):
        if not self.prestito:
            self.prestito = "Prestato"
            return "Il libro è stato prestato."
        else:
            return "Il libro è già stato prestato."

    def restuisci(self):
        if self.prestito:
            self.prestito = "Non prestato"
            return "Il libro è stato restituito"

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return "Il libro è aggiunto."

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                return libro.presta
        return "Il prestito è andato a buon fine."

    def mostra_libri_disponibili(self):
        libri_disponibili = [libro.titolo for libro in self.catalogo if not libro.prestito]
        if libri_disponibili:
            return libri_disponibili
        else:
            return "Non ci sono libri disponibili"

biblioteca = Biblioteca()

libro1 = Libro("Il piccolo principe", "Pietro Smith")

print(biblioteca.aggiungi_libro(libro1))

print(biblioteca.presta_libro(libro1))

print(libro1.restuisci())

print(biblioteca.mostra_libri_disponibili())


#eserciziocatalogofilm:

class MovieCatalog:
    def __init__(self):
        self.catalog = {}

    def add_movie(self, director_name, movies):
        if director_name not in self.catalog:
            self.catalog[director_name] = []
        self.catalog[director_name].extend(movies)
        return "Film aggiunti al catalogo."

    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog and movie_name in self.catalog[director_name]:
            self.catalog[director_name].remove(movie_name)
            if not self.catalog[director_name]:
                del self.catalog[director_name]
                return "Rimosso il regista"
        else:
            return  "Il film non è nel catalogo"

    def list_directors(self):
        return list(self.catalog.keys())

    def get_movies_by_director(self, director_name):
        if director_name in self.catalog:
            return self.catalog[director_name]
        else:
            return "Nessun film trovato per questo regista."

    def search_movies_by_title(self, title):
        results = {}
        for director, movies in self.catalog.items():
            for movie in movies:
                if title.lower() in movie.lower():
                    if director not in results:
                        results[director] = []
                    results[director].append((movie))
        return results if results else "Nessun film trovato con questo titolo."

#Per finire l'esercizio scrivere il dizionario e la print