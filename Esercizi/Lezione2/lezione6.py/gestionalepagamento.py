"""
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.
"""
class Pagamento:
    def __init__(self):   
        self.__importo = 0.0  # Attributo privato che memorizza l'importo del pagamento

    def set_importo(self, importo):
        if importo < 0:
            raise ValueError("L'importo non può essere negativo")
        else:
            self.__importo = float(importo)

    def get_importo(self):
        return self.__importo

    def dettagli_pagamento(self):
        print(f"Importo del pagamento: €{self.__importo:.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__()
        self.set_importo(importo)

    def dettagli_pagamento(self):
        print(f"Pagamento in contanti. Importo del pagamento: €{self.get_importo():.2f}")

    def in_pezzi_da(self):
        importo = self.get_importo()
        pezzi = [500, 200, 100, 50, 20, 10, 5,2, 1, 0.50, 0.20, 0.10 , 0.05, 0.01]
        for pezzo in pezzi:
            numero_pezzi = int(importo // pezzo)    
            importo= round(importo - numero_pezzi*pezzo, 2)
            #definire if for e la printa dato che non stampa.
            if numero_pezzi!=0 and pezzo >= 5:   
                print(f"Paga in banconote da {pezzo} numero_pezzi: {numero_pezzi}")
            elif numero_pezzi!=0 and pezzo < 5:  
                print(f"Paga in monete da {pezzo} numero_pezzi: {numero_pezzi}")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo, nome_titolare, data_scadenza, numero_carta):
        super().__init__()
        self.set_importo(importo)
        self.nome_titolare = nome_titolare
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta

    def dettagli_pagamento(self):
        print(f"Pagamento con carta di credito.\n"
              f"Nome del titolare: {self.nome_titolare}\n"
              f"Data di scadenza: {self.data_scadenza}\n"
              f"Numero della carta: {self.numero_carta}\n"
              f"Importo del pagamento: €{self.get_importo():.2f}")

# Test delle classi
pagamento1 = PagamentoContanti(123.56)
pagamento1.dettagli_pagamento()
pagamento1.in_pezzi_da()

pagamento2 = PagamentoContanti(789.99)
pagamento2.dettagli_pagamento()
pagamento2.in_pezzi_da()

pagamento3 = PagamentoCartaDiCredito(456.78, "Mario Rossi", "12/24", "1234 5678 9101 1121")
pagamento3.dettagli_pagamento()

pagamento4 = PagamentoCartaDiCredito(912.34, "Luigi Bianchi", "11/25", "9876 5432 1098 7654")
pagamento4.dettagli_pagamento()