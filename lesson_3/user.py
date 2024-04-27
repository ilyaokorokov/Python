class User:

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def sayName(self):
        print(self.fname)

    def saySurname(self):
        print(self.lname)

    def sayPerson(self):
        print(self.lname + ' ' + self.fname)
