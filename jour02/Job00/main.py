class Personne:

    def __init__(self, firstname, lastname) -> None:
        self._firstname = firstname
        self._lastname = lastname 

    def SePresenter(self):
        print(self.firstname + " " + self.lastname)

    def get_firstname(self):
        return self._firstname
    def get_lastname(self):
        return self._lastname
    def set_firstname(self, firstname):
        self._firstname = firstname
    def set_lastname(self, lastname):
        self._lastname = lastname    

    firstname = property(get_firstname, set_firstname)
    lastname = property(get_lastname, set_lastname)

p1 = Personne('Gon' , 'Freecs')
p2 = Personne('Hisoka', 'Le Magicien')

p1.SePresenter()
p2.SePresenter()

