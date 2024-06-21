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



#esercizi lez8 p.Giorgi 
from abc import ABC, abstractmethod
import math


# Creazione della classe astratta Shape
class Shape(ABC):

    # Metodo astratto area
    @abstractmethod
    def area(self):
        pass

    # Metodo astratto perimetro
    @abstractmethod
    def perimeter(self):
        pass

# Creazione della sottoclasse Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementazione del metodo area per Circle
    def area(self):
        return math.pi * (self.radius ** 2)

    # Implementazione del metodo perimetro per Circle
    def perimeter(self):
        return 2 * math.pi * self.radius

# Creazione della sottoclasse Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementazione del metodo area per Rectangle
    def area(self):
        return self.width * self.height

    # Implementazione del metodo perimetro per Rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)
class MathOperations:
    # Metodo statico per l'addizione
    @staticmethod
    def add(num1, num2):
        return num1 + num2


    # Metodo statico per la moltiplicazione
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

# Test dei metodi statici
print(MathOperations.add(5,3)) # Stampa: 8
print(MathOperations.multiply(5, 3)) # Stampa: 15

#eserciziosistema università 

from abc import ABC, abstractmethod

# Classe astratta Person
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Metodo astratto get_role
    @abstractmethod
    def get_role(self):
        pass

    # Metodo __str__
    def __str__(self):
        return f'{self.name}, {self.age} anni'

# Sottoclasse Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    # Metodo per iscriversi a un corso
    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

    # Implementazione del metodo astratto get_role
    def get_role(self):
        return 'Studente'

# Sottoclasse Professor
class Professor(Person):
    def __init__(self, name, age, professor_id, department):
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses = []

    # Metodo per assegnare un corso
    def assign_to_course(self, course):
        self.courses.append(course)
        course.set_professor(self)

    # Implementazione del metodo astratto get_role
    def get_role(self):
        return 'Professore'

# Classe Course
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.professor = None

    # Metodo per aggiungere uno studente
    def add_student(self, student):
        self.students.append(student)

    # Metodo per assegnare un professore
    def set_professor(self, professor):
        self.professor = professor

    # Metodo __str__
    def __str__(self):
        return f'{self.course_name} ({self.course_code})'

# Classe Department
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []
        self.professor = []

    # Metodo per aggiungere un corso
    def add_course(self, course):
        self.courses.append(course)

    # Metodo per aggiungere un professore
    def add_professor(self, professor):
        self.professor.append(professor)

    # Metodo __str__
    def __str__(self):
        return  self.department_name

# Classe University
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []

    # Metodo per aggiungere un dipartimento
    def add_student(self, student):
        self.students.append(student)
    # Metodo __str__
    def __str__(self):  
        return self.name    
###########ESERCIZIODELLERICETTE:####################################################################################################################
class RecipeManager:
    def __init__(self):
        self.recipes: dict={}
       
    def create_recipe(self, name: str, ingredients: list):
        if name not in self.recipes:
            self.recipes[name]=ingredients
        return self.recipes
   
    def add_ingredient(self, recipe_name:str ,ingredient: str):
        if recipe_name in self.recipes:
            if ingredient not in self.recipes[recipe_name]:
                self.recipes[recipe_name].append(ingredient)
                return self.recipes
   
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name].remove(ingredient)
                return self.recipes
               
               
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name in self.recipes:
            if old_ingredient in self.recipes[recipe_name]:
                updated_recipe = []
                for ingredient in self.recipes[recipe_name]:
                    if ingredient == old_ingredient:
                        updated_recipe.append(new_ingredient)
                    else:
                        updated_recipe.append(ingredient)
                self.recipes[recipe_name] = updated_recipe
                return self.recipes
            else:
                print('Errore: Ingrediente non presente')
        else:
            print('Errore: Ricetta non presente')

               
    def list_recipes(self):
        lista_ricette=[]
        for k in self.recipes.keys():
            lista_ricette.append(k)
        return lista_ricette
       
    def list_ingredients(self, recipes_name):
        if recipes_name in self.recipes:
            return self.recipes[recipes_name]
        else:
            print('errore la ricetta non esiste')
   
    def search_recipe_by_ingredient(self, ingredient):
        new_dict={}
        for k,v in self.recipes.items():
            if ingredient in self.recipes[k]:
                new_dict[k]=v
            return new_dict
            
    
    
######################esercizio animali##############à
class Specie:
    def __init__(self, nome, popolazione_iniziale, tasso_crescita):
        self.nome = nome
        self.popolazione = popolazione_iniziale
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        # Aggiorna la popolazione per l'anno successivo
        self.popolazione = int(self.popolazione *  (1 + self.tasso_crescita / 100))

    def anni_per_superare(self, altra_specie):
        anni = 0
        # Continua ad aggiornare la popolazione finché la popolazione di questa specie non supera quella dell'altra
        while self.popolazione <= altra_specie.popolazione and anni < 1000:
            self.cresci()
            altra_specie.cresci()
            anni += 1
        return anni

    def getDensita(self, area_kmq):
        anni = 0
        # Continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
        while self.popolazione / area_kmq < 1 and anni < 1000:
            self.cresci()
            anni += 1
        return anni


class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale, tasso_crescita):
        # Inizializza il nome della specie
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)


class Elefante(Specie):
    def __init__(self, popolazione_iniziale, tasso_crescita):
        # Inizializza il nome della specie
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)

##eserciziocontatore##
class Contatore:
    # Metodo costruttore che inizializza il conteggio a 0
    def __init__(self):
        self.conteggio = 0

    # Metodo per impostare il conteggio a 0
    def setZero(self):
        self.conteggio = 0

    # Metodo per incrementare il conteggio di 1
    def add1(self):
        self.conteggio += 1

    # Metodo per decrementare il conteggio di 1, con controllo per non andare sotto 0
    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            # Stampa un messaggio di errore se il conteggio è già 0
            print("Non è possibile eseguire la sottrazione")

    # Metodo per ottenere il valore corrente del conteggio
    def get(self):
        return self.conteggio

    # Metodo per mostrare il valore corrente del conteggio
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")
#ultimi esercizi cascio:
#Esempio di utilizzo del DatabaseDate
if name == "__main":
    db = DatabaseDate()

    try:
        db.aggiungi_data("01.01.2023")
        db.aggiungi_data("15.06.2023")
        db.aggiungi_data("31.12.2023")
        print("Date nel database:", db.dates)

        db.elimina_data("15.06.2023")
        print("Date nel database dopo eliminazione:", db.dates)

        db.modifica_data("01.01.2023", "01.01.2024")
        print("Date nel database dopo modifica:", db.dates)

        risultato_query = db.query_data("31.12.2023")
        print("Risultato query:", risultato_query)

    except ValueError as e:
        print(f"Errore: {e}")
#Esercizio 3
import unittest

#Definizione dell'eccezione personalizzata
class FormulaError(Exception):
    pass

#Funzione per eseguire il calcolo
def calculate(input_str):
    # Split dell'input in una lista di elementi
    elements = input_str.split()

#Controllo se ci sono esattamente 3 elementi
    if len(elements) != 3:
        raise FormulaError("La formula deve essere composta da un numero, un operatore (+ o -), e un altro numero.")

#Estrazione degli elementi
    num1_str, operator, num2_str = elements

#Controllo dell'operatore
    if operator not in ('+', '-'):
        raise FormulaError("L'operatore supportato è solo + o -.")

#Tentativo di conversione dei numeri in virgola mobile
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        raise FormulaError("I numeri devono essere numerici e separati da spazi.")

#Esecuzione del calcolo in base all'operatore
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2

#Restituzione del risultato
    return result

#Test case usando unittest per verificare diverse casistiche
class TestCalculate(unittest.TestCase):

    def test_valid_input_addition(self):
        result = calculate("5 + 3")
        self.assertEqual(result, 8)

    def test_valid_input_subtraction(self):
        result = calculate("10 - 4")
        self.assertEqual(result, 6)

    def test_invalid_number_of_elements(self):
        with self.assertRaises(FormulaError):
            calculate("5 + 3 + 2")

    def test_invalid_operator(self):
        with self.assertRaises(FormulaError):
            calculate("5 * 3")

    def test_invalid_number_format(self):
        with self.assertRaises(FormulaError):
            calculate("5 + hello") 
def testmixedvalidity(self):
        with self.assertRaises(FormulaError):
            calculate("5 +")   
def testfloatnumbers(self):
        result = calculate("3.5 + 2.5")
        self.assertEqual(result, 6.0)

def test_negative_numbers(self):
        result = calculate("5 - 8")
        self.assertEqual(result, -3)
def test_zero_result(self):
        result = calculate("5 - 5")
        self.assertEqual(result, 0)

def test_large_numbers(self):
        result = calculate("1000000 + 500000")
        self.assertEqual(result, 1500000)

#Esecuzione dei test
if __name == '__main':
    unittest.main()

#Ciclo per eseguire il calcolatore interattivo
while True:
    try:
        user_input = input("Inserisci una formula (o 'quit' per uscire): ")

        if user_input.lower() == 'quit':
            break

        result = calculate(user_input)
        print(f"Risultato: {result}")

    except FormulaError as e:
        print(f"Errore: {e}")
E infine l'esercizio 4 
Definizione di eccezioni personalizzate
class FractionError(Exception):
    pass


class ZeroDenominatorError(FractionError):
    def init(self):
        super().init("Il denominatore non può essere zero.")


class UnsupportedOperationError(FractionError):
    def init(self, operation):
        super().init(f"L'operazione '{operation}' non è supportata.")


class Fraction:
    def init(self, numerator, denominator):
        try:
            if denominator == 0:
                raise ZeroDenominatorError()
            self.numerator = numerator
            self.denominator = denominator
            self.simplify()
        except ZeroDivisionError:
            raise ZeroDenominatorError()
        except Exception as e:
            raise FractionError(f"Errore durante la creazione della frazione: {str(e)}")

    def simplify(self):
        try:
            gcd_val = self.gcd(self.numerator, self.denominator)
            self.numerator //= gcd_val
            self.denominator //= gcd_val
            # Assicurarsi che il denominatore sia positivo per convenzione
            if self.denominator < 0:
                self.numerator = -self.numerator
                self.denominator = -self.denominator
        except Exception as e:
            raise FractionError(f"Errore durante la semplificazione della frazione: {str(e)}")

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
def str(self):
        return f"{self.numerator}/{self.denominator}"

def eq(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

def add(self, other):
        if not isinstance(other, Fraction):
            raise UnsupportedOperationError('+')
        try:
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        except Exception as e:
            raise FractionError(f"Errore durante l'addizione delle frazioni: {str(e)}")

def sub(self, other):
        if not isinstance(other, Fraction):
            raise UnsupportedOperationError('-')
        try:
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        except Exception as e:
            raise FractionError(f"Errore durante la sottrazione delle frazioni: {str(e)}")

def mul(self, other):
        if not isinstance(other, Fraction):
            raise UnsupportedOperationError('')
        try:
            new_numerator = self.numerator other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        except Exception as e:
            raise FractionError(f"Errore durante la moltiplicazione delle frazioni: {str(e)}")
def truediv(self, other):
        if not isinstance(other, Fraction):
            raise UnsupportedOperationError('/')
        try:
            if other.numerator == 0:
                raise ZeroDenominatorError()
            newnumerator = self.numerator * other.denominator
            newdenominator = self.denominator * other.numerator
            return Fraction(newnumerator, newdenominator)
        except ZeroDivisionError:
            raise ZeroDenominatorError()
        except Exception as e:
            raise FractionError(f"Errore durante la divisione delle frazioni: {str(e)}")


#Test di esempio
if __name == "__main":
    try:
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)

        print(f"f1 = {f1}")
        print(f"f2 = {f2}")

        print(f"f1 + f2 = {f1 + f2}")
        print(f"f1 - f2 = {f1 - f2}")
        print(f"f1 * f2 = {f1 * f2}")
        print(f"f1 / f2 = {f1 / f2}")

        print(f"f1 == f2: {f1 == f2}")
    except FractionError as e:
        print(f"Errore: {e}")
