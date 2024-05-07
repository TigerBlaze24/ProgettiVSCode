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