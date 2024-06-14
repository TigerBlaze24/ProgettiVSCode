"""Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
 """
from persona import Persona
class Paziente:
    def __init__(self, first_name:str, last_name:str,__idcode:int):   
        super().__init__(first_name, last_name) 
    def setIdCode(self):    
        return self.__idcode    
    def getIdcode(self):    
        return self.__idcode    
    def patientInfo(self):  
        print(f"Paziente: {self.getName()} {self.getLastname()}!") 
        print(f"ID: {self.getIdcode()} !")   



    
