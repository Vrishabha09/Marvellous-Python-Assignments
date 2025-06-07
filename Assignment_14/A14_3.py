
class Book:
    def __init__(self):
        self.__price = 0

    def getPrice(self):
        return self.__price
    
    def setPrice(self,p):
        self.__price = p


def main():
    bobj = Book()
    bobj.setPrice(1000)
    Price = bobj.getPrice()
    print("Price of book :",Price)

if(__name__ == "__main__"):
    main()