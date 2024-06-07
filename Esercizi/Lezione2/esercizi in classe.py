#bozza esercizio lista palindromo
class Node:
    def _init_(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        # Find the middle of the linked list
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare the first and second half nodes
        first_half = self.head
        second_half = prev
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next

        # Optional: Restore the original list (if needed)
        # current = prev
        # prev = None
        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node

        return True
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(2)
linked_list.append(1)
print(linked_list.is_palindrome())  # Output: True
#####################################################################
"""Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- C Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto.
"""
class Media:
 def __init__ ( self,tile:str,reviews:list,media:int,voto:int):
    self.title = str
    self.reviews = list
    self.voto= int
    self.media = int
 def set_title(self,imposttitle):
    self.title= imposttitle
    return imposttitle
def get_title(self,gettitle):
    self.gettitle=gettitle
    return gettitle
def getmedia(self,media):
    self.media= media
    return media
def aggiungi_valutazione(self,voto):
    self.aggiungivalutazione =voto
    return voto
def get_rate(self,rate):
    if rate==1:
     return"terribile"
    elif rate==2:
     return"normale"
    elif rate==3:
     return"normale"
    elif rate==4:
     return"bello"
    elif rate==5:   
       return"grandioso"       
def percentage(self,voto :int):
#da finire a casa
   
   
     


