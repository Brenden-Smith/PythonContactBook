class Contacts():
    def __init__(self):
        self.n = 0
        self.s = 0
        self.book = {0 : {"sorted name": {"first name" : None, "last name" : None, "phone" : None, "address" : None}}}

    def add(self, firstName : str, lastName : str, phoneNumber : str, address : str) :
        if self.s == 1:
            sname = lastName
        else:
            sname = firstName
        self.book[self.n] = {sname: {"first name" : firstName, "last name" : lastName, "phone" : phoneNumber, "address" : address}}
        self.n += 1

    def remove(self, firstName : str, lastName : str):
        if self.n == 0: return IndexError("The contact book is empty")
        p = self.book

    def view(self):
        for x in range(0,self.n):
            print("---------")
            print("Position:", x)
            print("First Name:", self.book[x]["first name"])
            print("Last Name:", self.book[x]["last name"])
            print("Phone Number:", self.book[x]["phone"])
            print("Address:", self.book[x]["address"])
        print("---------")

    def sortByFirst(self):
        p = self.book

    def sortByLast(self):
        p = sorted((self.book).items(), key=lambda x: x[1], reverse=True)

        for i in p:
            print(i[0], i[1])





