class Contacts():
    def __init__(self):
        self.n = 0
        self.book = {self.n : {"first name" : None, "last name" : None, "phone" : None, "address" : None}}

    def add(self, firstName : str, lastName : str, phoneNumber : str, address : str) :
        self.book[self.n] = {"first name" : firstName, "last name" : lastName, "phone" : phoneNumber, "address" : address}
        self.n += 1
    def remove(self, firstName : str, lastName : str):
        if self.n == 0: return IndexError("The contact book is empty")

    def view(self):
        for x in range(0,self.n):
            print("---------")
            print("First Name:", self.book[x]["first name"])
            print("Last Name:", self.book[x]["last name"])
            print("Phone Number:", self.book[x]["phone"])
            print("Address:", self.book[x]["address"])
        print("---------")