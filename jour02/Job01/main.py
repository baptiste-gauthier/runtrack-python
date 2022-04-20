class Personne:

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

class Book:

    def __init__(self, title: str, author: object) -> None:
        self.title = title
        self.author = author

    def DisplayTitle(self):
        print(self.title)


class Author(Personne):

    def __init__(self, firstname: str, lastname: str, collection: list[str]) -> None:
        Personne.__init__(self, firstname, lastname)
        self.collection = collection 

    def writeBook(self,title):
        self.collection.append(title)

    def listCollection(self):
        return self.collection


author = Author('Baptiste', 'Gauthier', [])
author.writeBook('Mon premier livre')
author.writeBook('Mon second livre')

author2 = Author('Gon', 'Freecs', [])
author2.writeBook('Guide du hunter')
author2.writeBook('Tuto canne a peche')
author2.writeBook('Apprendre le nen')

book = Book('titre' , author)
print(book.author.firstname)

print('Listes des livres de' , author.firstname + ' ' + author.lastname)
print(author.listCollection())
print('Listes des livres de' , author2.firstname + ' ' + author2.lastname)
print(author2.listCollection())





        
  


