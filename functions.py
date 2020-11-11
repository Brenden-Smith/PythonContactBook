class Contacts():
    def __init__(self):
        self.n = 0
        self.s = 0 # 0 = First Name, 1 = Last Name
        self.book = {"sorted name": {"first name" : None, "last name" : None, "phone" : None, "address" : None}}

    def add(self, firstName : str, lastName : str, phoneNumber : str, address : str) :
        if self.s == 1:
            sname = lastName
        else:
            sname = firstName
        self.book[sname] = {"first name" : firstName, "last name" : lastName, "phone" : phoneNumber, "address" : address}
        self.n += 1

    def remove(self, firstName : str, lastName : str):
        if self.n == 0: return IndexError("The contact book is empty")
        if self.s == 1: sname = lastName
        else: sname = firstName
        if self.book.get(sname)
        p = self.book
        self.n -= 1

    def search(self, name):
        if self.book.get(name):
            print("---------")
            print("First Name:", self.book[name]["first name"])
            print("Last Name:", self.book[name]["last name"])
            print("Phone Number:", self.book[name]["phone"])
            print("Address:", self.book[name]["address"])
            print("---------")
        else:
            print("This contact could not be found")

    def view(self):
        if self.n == 0:
            print("The contact book is empty")
        else:
            for x in self.book:
                if self.book[x]["first name"] != None:
                    print("---------")
                    print("First Name:", self.book[x]["first name"])
                    print("Last Name:", self.book[x]["last name"])
                    print("Phone Number:", self.book[x]["phone"])
                    print("Address:", self.book[x]["address"])
            print("---------")

    def sortByFirst(self):
        p = self.book

    def sortByLast(self):
        p = self.book
        n = self.book.

        for i in p:
            print(i[0], i[1])





