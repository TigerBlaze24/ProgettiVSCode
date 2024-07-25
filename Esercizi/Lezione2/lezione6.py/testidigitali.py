class Documento:    
    def __init__(self,text):
        self.testo: str= text  
    def getText(self):     
        return self.text
    def setText(self, text):        
        self.text = text

    def ilsnText(self,key):
        if key in self.text:
            return True 
        else:   
            if key not in self.text:    
                return False
    
    def setscriviTestonelFile(self,path,key): 
        file = open(path,"w")
        file.write(self.getText())
        file.close()(self,key)
        if key in self.text:
            return True
        else:   
            if key not in self.text:    
                return False
#mi eredito con la super la classe precedente
class Email(Documento):
    def __init__(self,mittente,destinatario,titolo,text):
        super().__init__(text)
        self.mittente = mittente
        self.destinatario=destinatario
        self.titolo=titolo
        self.text=text 
        #definisco il set per permettere di aggiornare i dati
    def setMittente(self, mittente):     
        self.mittente = mittente
    def setDestinatario(self, destinatario):     
        self.destinatario = destinatario
    def setTitolo(self, titolo):     
        self.titolo = titolo
    def setText(self, text):     
        self.text = text    

    def getMittente(self):     
        return self.mittente
    def getDestinatario(self):     
        return self.destinatario
    def getTitolo(self):     
        return self.titolo
    #NB I PARAMETRI EREDITATI NON SI RISETTANO E GETTANO!ES(TEXT ORA)
    #ora concateno i parametri:   
    def getText(self):  
        text=f"Mittente:{self.getMittente()}, Destinatario:{self.getDestinatario}\n"
        text=f"Titolo:{self.getTitolo()}\n"
        text=f"Testo del messaggio :{super().getText()}\n"  
        return text
    #per aprire e scrivere un file e chiuderlo, Path=titolo del file
    def setscriviTestonelFile(self,path): 
        file = open(path,"w")
        file.write(self.getText())
        file.close()
#da scrivere lettura UGUALE E FINIRE LESERCIZIO
            
    

    class File(Documento):  
     def __init__(self,nome_percorso) -> None:
            self.nome_percorso=nome_percorso    
            super().__init__(self.leggiTestoDaFile)   

def leggiTestoDaFiledef(self,path): 
            file = open(path,"w")
            file.write(self.getText())
            file.close()

d = Documento("Ciao")
d.setText("ciao")
print(d.getText())
print(d.ilsnText("a"))
e = Email(mittente="", destinatario="", titolo="", text="")
e.setMittente("cuanbellina@alice.it")
e.setDestinatario("bob@vattelapesca")
e.setTitolo("cena")
e.setText("ciao bob vieni stasera a cena fuori?")
print(e.getText())
        

#fare vedere errori a dylan



        
        
