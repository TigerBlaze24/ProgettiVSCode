#2)
def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)  # dp[i] sarà True se s[0:i] può essere segmentato utilizzando il dizionario
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[-1]  # Restituisce True se l'intera stringa può essere segmentata, altrimenti False
#3)
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.borrow()

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        self.books[book_id] = Book(book_id, title, author)

    def register_member(self, member_id, name):
        self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            member.borrow_book(book)

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            member.return_book(book)

    def get_borrowed_books(self, member_id):
        member = self.members.get(member_id)
        if member:
            return [book.title for book in member.borrowed_books]
#4)class Account:
    def __init__(self, account_id):s
        self.account_id = account_id
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id):
        self.accounts[account_id] = Account(account_id)
        return self.accounts[account_id]

    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
#1)
class ListNode:
    def __init__(self, val=0, next=Nome):
        self.val = val
        self.next = next

def inverti_lista(nodo):
    prev = None
    current = nodo
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    nodo = prev
    return nodo

# Funzione per stampare la lista concatenata
def stampa_lista(nodo):
    while(nodo):
        print(nodo.val),
        nodo = nodo.next


# Funzione per stampare la lista concatenata
def stampa_lista(nodo):
    while(nodo):
        print(nodo.dato),
        nodo = nodo.prossimo

# Creazione della lista concatenata
nodo1 = Nodo('A')
nodo2 = Nodo('B')
nodo3 = Nodo('C')
nodo4 = Nodo('D')

nodo1.prossimo = nodo2
nodo2.prossimo = nodo3
nodo3.prossimo = nodo4

