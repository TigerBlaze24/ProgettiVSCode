class Elettrodomestico:
  def _init__(self, marca: str, modello: str, potenza: int):    
    self.marca = marca  
    self.modello = modello
    self.potenza = potenza  

    def descrivi_elettrodomestico(self):
      print  (f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W")

class Frigorifero(Elettrodomestico):
  def _init__(self, marca: str, modello: str, potenza: int , capacita:int):
    super().__init__(marca,modello,potenza)
    self.capacita = capacita    

    def descrivi_elettrodomestico(self):
      print  (f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}w,Capacita:{self.capacita}L") 

class Lavatrice(Elettrodomestico):  
  
  def _init__(self, marca: str, modello: str, potenza: int , capacita:int,carico_max: int):
    super().__init__(marca,modello,potenza)
    self.carico_max = carico_max

    def descrivi_elettrodomestico(self):
      print  (f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}w,Carico massimo: {self.carico_max}kg")
  



  