#1)Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    
    dizionario: dict = {}
    
    for key, value in prodotti.items():
        
        if prodotti[key] > 20:
            
            dizionario[key] = prodotti[key] - (prodotti[key] * 0.1)
            
    return dizionario

#2)Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    sum: int = 0
    
    for num in numbers:
        
        if num > threshold:
            sum += num
            
    return sum

#3)Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codie
    dizionario: dict = {}
    for t in tuples:
        
        key = t[0]
        
        if key in dizionario:
            
            dizionario[key].append(t[1])
            
        else:
            
            dizionario[key] = [t[1]]
            
    return dizionario
#4
# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
#per commentare tutto insieme :ctrl+freccia+7
# if x % 2 == 0:
#   x //= 2
# else:
#   x = 3*x - 1   
#   return x
#5)progettazione accauntbancario:
class Account:
    def __init__(self, accaunt_id:str, balance:float):  
        self.accaunt_id = accaunt_id
        self.balance = balance  

    def deposit(self, amount: float):
        self.balance = amount

    def get_balance(self):   
        return self.balance
    
class Bank:
    def __init__(self):
        
        self.accounts = {}

    def create_account(self, account_id):
        
        if account_id in self.accounts:
            
            print("Account with this ID already exists")
            return None
        
        new_account = Account(account_id, 0)
        self.accounts[account_id] = new_account
        
        return new_account

    def deposit(self, account_id, amount):

        self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id):
        
        if account_id not in self.accounts:
             print("Account not found")     
             return None

        return self.accounts[account_id].get_balance()

#6)In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca  # Assegna la marca del veicolo all'attributo dell'oggetto
        self.modello = modello  # Assegna il modello del veicolo all'attributo dell'oggetto
        self.anno = anno  # Assegna l'anno del veicolo all'attributo dell'oggetto

    def descrivi_veicolo(self):
        # Stampa una descrizione del veicolo includendo marca, modello e anno
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)  # Chiama il costruttore della classe base Veicolo
        self.numero_porte = numero_porte  # Assegna il numero di porte all'attributo dell'oggetto

    def descrivi_veicolo(self):
        # Stampa una descrizione dell'auto includendo marca, modello, anno e numero di porte
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")


class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)  # Chiama il costruttore della classe base Veicolo
        self.tipo = tipo  # Assegna il tipo di moto all'attributo dell'oggetto

    def descrivi_veicolo(self):
        # Stampa una descrizione della moto includendo marca, modello, anno e tipo
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")


# Test delle classi
veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto


# Test case aggiuntivi
veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
auto2 = Auto("Honda", "Civic", 2019, 5)  # Crea un'altra istanza della classe Auto
moto2 = Moto("Ducati", "Panigale", 2023, "superbike")  # Crea un'altra istanza della classe Moto

# Verifica che le descrizioni siano corrette
veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
auto2.descrivi_veicolo()  # Test del metodo descrivi_veicolo per una seconda Auto
moto2.descrivi_veicolo()  # Test del metodo descrivi_veicolo per una seconda Moto

#7)Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or (conditionB and conditionC):
        
        return "Operazione permessa"
        
    else:
        
        return "Operazione negata"
    
#8)Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dizionario: dict = {"pari": [], "dispari": []}
    
    for numero in lista:
        
        if numero % 2 == 0:
            
            dizionario["pari"].append(numero)
            
        else:
            
            dizionario["dispari"].append(numero)
            
            
    return dizionario

#9)Progettare un sistema di gestione della biblioteca:
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise ValueError(f"Book is already borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            raise ValueError(f"Book is already borrowed")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)    
            book.return_book()
        else:
            raise ValueError(f"Book not borrowed by this member")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        self.books[book_id] = Book(book_id, title, author)

    def register_member(self, member_id, name):
        self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            member.borrow_book(book)
        elif not member:
            raise ValueError(f"Member not found")
        elif not book:
            raise ValueError(f"Book not found")

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            member.return_book(book)

    def get_borrowed_books(self, member_id):
        member = self.members.get(member_id)
        if member:
            return [book.title for book in member.borrowed_books]

#10)Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".
def check_access(username: str, password: str, is_active: bool) -> str:
    
    if username == "admin" and password == "12345" and is_active:
        
        return "Accesso consentito"
    
    else:
        
        return "Accesso negato"














#15)
class RecipeManager:
    # Costruttore della classe RecipeManager
    def __init__(self):
        # Dizionario che contiene i nomi delle ricette come chiavi e la lista degli ingredienti come valori
        self.recipes: dict[str, list[str]] = {}

    # Metodo per creare una nuova ricetta
    def create_recipe(self, name: str, ingredients: list[str]) -> dict[str, list[str]]:
        # Se la ricetta non esiste già, la aggiungo al dizionario
        if name not in self.recipes:
            # La chiave è il nome della ricetta, il valore è la lista degli ingredienti
            self.recipes[name] = ingredients
            # Restituisco un dizionario con il nome della ricetta come chiave e la lista degli ingredienti come valore
            return {name: ingredients}
        else:
            # Se la ricetta esiste già, restituisco un messaggio di errore
            return f"Recipe '{name}' already exists."

    # Metodo per aggiungere un ingrediente a una ricetta
    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]:
        # Se la ricetta esiste
        if recipe_name in self.recipes:
            # Se l'ingrediente non è già presente nella lista degli ingredienti
            if ingredient not in self.recipes[recipe_name]:
                # Aggiungo l'ingrediente alla lista degli ingredienti
                self.recipes[recipe_name].append(ingredient)
                # Restituisco un dizionario con il nome della ricetta come chiave e la lista degli ingredienti come valore
                return {recipe_name: self.recipes[recipe_name]}
            else:
                # Se l'ingrediente è già presente nella lista degli ingredienti, restituisco un messaggio di errore
                return f"Ingredient '{ingredient}' already exists in '{recipe_name}'."
        else:
            # Se la ricetta non esiste, restituisco un messaggio di errore
            return f"Recipe '{recipe_name}' does not exist."

    # Metodo per rimuovere un ingrediente da una ricetta
    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list[str]]:
        # Se la ricetta esiste
        if recipe_name in self.recipes:
            # Se l'ingrediente è presente nella lista degli ingredienti
            if ingredient in self.recipes[recipe_name]:
                # Rimuovo l'ingrediente dalla lista degli ingredienti
                self.recipes[recipe_name].remove(ingredient)
                # Restituisco un dizionario con il nome della ricetta come chiave e la lista degli ingredienti come valore
                return {recipe_name: self.recipes[recipe_name]}
            else:
                # Se l'ingrediente non è presente nella lista degli ingredienti, restituisco un messaggio di errore
                return f"Ingredient '{ingredient}' not found in '{recipe_name}'."
        else:
            # Se la ricetta non esiste, restituisco un messaggio di errore
            return f"Recipe '{recipe_name}' does not exist."

    # Metodo per aggiornare un ingrediente di una ricetta
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict[str, list[str]]:
        #  Se la ricetta esiste
        if recipe_name in self.recipes:
            # Se l'ingrediente da sostituire è presente nella lista degli ingredienti
            if old_ingredient in self.recipes[recipe_name]:
                # Trovo l'indice dell'ingrediente da sostituire
                idx = self.recipes[recipe_name].index(old_ingredient)
                # Sostituisco l'ingrediente
                self.recipes[recipe_name][idx] = new_ingredient
                # Restituisco un dizionario con il nome della ricetta come chiave e la lista degli ingredienti come valore
                return {recipe_name: self.recipes[recipe_name]}
            else:
                # Se l'ingrediente da sostituire non è presente nella lista degli ingredienti, restituisco un messaggio di errore
                return f"Ingredient '{old_ingredient}' not found in '{recipe_name}'."
        else:
            # Se la ricetta non esiste, restituisco un messaggio di errore
            return f"Recipe '{recipe_name}' does not exist."

    # Metodo per eliminare una ricetta
    def list_recipes(self) -> list[str]:
        # Restituisco la lista dei nomi delle ricette
        return list(self.recipes.keys())

    # Metodo per visualizzare gli ingredienti di una ricetta
    def list_ingredients(self, recipe_name: str) -> list[str]:
        # Se la ricetta esiste, restituisco la lista degli ingredienti
        if recipe_name in self.recipes:
            # Restituisco la lista degli ingredienti
            return self.recipes[recipe_name]
        else:
            # Se la ricetta non esiste, restituisco un messaggio di errore
            return f"Recipe '{recipe_name}' does not exist."

    # Metodo per cercare una ricetta per ingrediente
    def search_recipe_by_ingredient(self, ingredient: str) -> dict[str, list[str]]:
        # Crea un dizionario vuoto che conterrà i risultati della ricerca.
        # Il dizionario avrà come chiavi i nomi delle ricette e come valori gli ingredienti.
        result :dict[str, list[str]] = {}

        # Itera su tutte le ricette memorizzate nell'attributo `self.recipes` dell'oggetto.
        for name, ingredients in self.recipes.items():
            # Controlla se l'ingrediente specificato è presente nella lista degli ingredienti della ricetta corrente.
            if ingredient in ingredients:
                # Se l'ingrediente è presente, aggiungi la ricetta corrente al dizionario dei risultati.
                # La chiave è il nome della ricetta e il valore è la lista degli ingredienti.
                result[name] = ingredients

        # Dopo aver esaminato tutte le ricette, controlla se il dizionario `result` contiene qualche risultato.
        if result:
            # Se ci sono risultati, ritornali.
            return result
        else:
            # Se non ci sono risultati, ritorna un messaggio che indica che non sono state trovate ricette
            # che contengono l'ingrediente specificato.
            return f"No recipes found with ingredient '{ingredient}'"


# Esempio di utilizzo:
manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"])) # {'Torta di mele': ['Farina', 'Uova', 'Mele']}
print(manager.add_ingredient("Torta di mele", "Zucchero")) # {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele")) # ['Farina', 'Uova', 'Mele', 'Zucchero']
print(manager.search_recipe_by_ingredient("Uova")) # {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}

manager = RecipeManager()
# Creazione di una nuova ricetta chiamata "Pizza Margherita"
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
# Output atteso: {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}

# Aggiunta di un ingrediente "Basilico" alla ricetta "Pizza Margherita"
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
# Output atteso: {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}

# Aggiornamento di un ingrediente da "Mozzarella" a "Mozzarella di Bufala" nella ricetta "Pizza Margherita"
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
# Output atteso: {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}

# Rimozione di un ingrediente "Acqua" dalla ricetta "Pizza Margherita"
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
# Output atteso: {'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}

# Visualizzazione degli ingredienti della ricetta "Pizza Margherita"
print(manager.list_ingredients("Pizza Margherita"))
# Output atteso: ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']


manager = RecipeManager()
# Creazione di una nuova ricetta chiamata "Spaghetti alla Carbonara"
print(manager.create_recipe("Spaghetti alla Carbonara", ["Spaghetti", "Uova", "Guanciale", "Pecorino Romano", "Pepe"]))
# Output atteso: {'Spaghetti alla Carbonara': ['Spaghetti', 'Uova', 'Guanciale', 'Pecorino Romano', 'Pepe']}

# Ricerca di ricette che contengono l'ingrediente "Uova"
print(manager.search_recipe_by_ingredient("Guanciale"))
# Output atteso: {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero'], 'Spaghetti alla Carbonara': ['Spaghetti', 'Uova', 'Guanciale', 'Pecorino Romano', 'Pepe']}

#16-Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def frequency_dict(elements:list) -> dict:
    
    dizionario: dict = {}
    
    for elem in elements: 
        
        if elem in dizionario:  
            dizionario[elem] += 1  
            
        else:
            dizionario[elem] = 1
        
    return dizionario

