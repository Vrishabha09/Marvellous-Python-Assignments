class BookStore:
    NoOfBooks = 0
    def __init__(self,n,a):
        self.Name = n
        self.Author = a
        self.NoOfBooks += 1

    def Display(self):
        print("Name :",self.Name,"| Author :",self.Author," | No of Books :",self.NoOfBooks)

def main():
    bobj = BookStore("Linux System Programming","Robert Love")
    bobj.Display();

    bobj1 = BookStore("C Programming","Dennis Ritchie")
    bobj1.Display();

if(__name__ == "__main__"):
    main()