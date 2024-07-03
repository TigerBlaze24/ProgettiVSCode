#esercizio 2
class DatabaseDate:
    def init(self):
        self.dates = {}  # Dizionario per memorizzare le date nel formato gg.mm.aaaa

    def aggiungi_data(self, data_str):
        """
        Aggiunge una nuova data al database.

        Args:
        

    data_str (str): Stringa rappresentante la data nel formato gg.mm.aaaa


        Raises:
        

    ValueError: Se la data è già presente nel database"""   
        if data_str in self.dates:
              raise ValueError("Data già presente nel database")
        self.dates[data_str] = True


    def elimina_data(self, data_str):
        """
        Elimina una data dal database.

        Args:
        

    data_str (str): Stringa rappresentante la data nel formato gg.mm.aaaa


        Raises:
        

    ValueError: Se la data non è presente nel database"""   
        if data_str not in self.dates:
              raise ValueError("Data non presente nel database")    
        def selfdates


    def modifica_data(self, data_str_vecchia, data_str_nuova):
        """
        Modifica una data nel database.

        Args:
        

    data_str_vecchia (str): Stringa rappresentante la data da modificare nel formato gg.mm.aaaa
        data_str_nuova (str): Nuova stringa rappresentante la data nel formato gg.mm.aaaa


        Raises:
        

    ValueError: Se la data da modificare non è presente nel database"""
        if data_str_vecchia not in self.dates:
              raise ValueError("Data da modificare non presente nel database")  
        
        if data_str_nuova in self.dates:
              raise ValueError("Nuova data già presente nel database")  
        self.elimina_data(data_str_vecchia)     
        self.aggiungi_data(data_str_nuova)

def querydata(self, datastr):
        """
        Esegue una query nel database per ottenere una data specifica.

        Args:
        

    data_str (str): Stringa rappresentante la data da cercare nel formato gg.mm.aaaa


        Returns:
        

    str: La data richiesta se presente nel database


        Raises:
        

    ValueError: Se la data non è presente nel database"""   
        if data_str not in self.dates:
              raise ValueError("Data non presente nel database")    
        return data_str 
#da fare vedere errori 
