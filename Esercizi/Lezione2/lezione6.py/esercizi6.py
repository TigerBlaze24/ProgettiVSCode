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
cane.get_legs(-3)
print(cane.get_legs)
      

