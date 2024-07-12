from abc import ABC
from abc import abstractmethod#per definire la classe astratta
class CodificaMessagio(ABC):
    @abstractmethod#(metodo astratto=decorator) 
    def Codifica(self,testoinchiaro):
            return self.testoinchiaro   
       
class DecodificaMessagio(ABC):
    @abstractmethod    
    def Decodifica(self,testocodificato):  
            return self.testocodificato
class cifratoreascorrimento(CodificaMessagio,DecodificaMessagio):   
      def __init__(self,chiave):    
            self.chiave = chiave
            
          
