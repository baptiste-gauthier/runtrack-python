class Personne:

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

class Author(Personne):

    def __init__(self, firstname: str, lastname: str, collection: list[str]) -> None:
        Personne.__init__(self, firstname, lastname)
        self.collection = collection 

    def writeBook(self,title):
        self.collection.append(title)

    def listCollection(self):
        return self.collection

class Book:

    def __init__(self, title: str, author: object, quantity : int) -> None:
        self.title = title
        self.author = author
        self.quantity = quantity


class Client(Personne):
    pass

class Bibliotheque:

    def __init__(self, name: str, collection: list[str]) -> None:
       self.name = name
       self.collection = collection

    def BuyBook(self, author: object, book : Book):
        if book.title in author.listCollection():
            self.collection.append(book.title)                                
        else:
            print('Ce livre n\'appartient pas à la liste de l\'auteur')      

    def Inventory(self):
        print('La bibiothèque contient actuellement' , len(self.collection) , 'livre')
        for book in self.collection:
            print(book)      

    def rent(self, client: object , book: object):
        if book.title in self.collection and book.quantity != 0:
            client.collection.append(book.title) 
            book.quantity = book.quantity - 1   
        else:
            print('Ce livre n\'existe pas ou n\'est plus en stock')    

    def giveBook(client: object):
        return 0 # a finir 



author1 = Author('Akira', 'Toriyama' , [])
author1.writeBook('Dragon Ball')
author1.writeBook('Dragon Ball Super')

# print(author1.listCollection())

book1 = Book('Dragon Ball', author1, 9)
book5 = Book('Dragon Ball Super', author1, 15)

biblio = Bibliotheque('Ma bibliotheque' , [])
biblio.BuyBook(author1 , book1)
biblio.Inventory()

author2 = Author('Jules', 'Verne' , [])
book2 = Book('20 000 lieues sous les mers', author2, 3)

author3 = Author('Alexandre', 'Dumas' , [])
book3 = Book('Les trois mousquetaires', author3, 5)

author4 = Author('Honoré ', 'de Balzac' , [])
book4 = Book('La peau de chagrin', author4, 0)

client = Client('Bruce' , 'Wayne')




