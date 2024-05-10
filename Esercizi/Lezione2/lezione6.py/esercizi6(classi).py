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
