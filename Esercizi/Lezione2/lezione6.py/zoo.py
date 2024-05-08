class Zoo:
   def __init__(self,fences,zoo_kypers):    
       self.fences = fences
       self.zoo_kypers = zoo_kypers       
class Animal:  
   def __init__(self, name,species,age,height, width, preferred_habitat, health):
       self.name = name
       self.species = species
       self.age = age
       self.height = height
       self.width = width
       self.preferred_habitat = preferred_habitat
       self.health =(100*(1/age)) 
class Fence:  
   def __init__(self, area,temperature,habitat):    
      self.area = area
      self.temperature = temperature
      self.habitat = habitat
class Zookepers:
   def __init__(self, nome,cognome,id):    
      self.nome = nome
      self.cognome = cognome
      self.id = id
zookepers=[Zookepers("Teo","Maggi",123)]
animal=Animal("Alex","leone",20,2.00, 4.00, "savana", 250)
      