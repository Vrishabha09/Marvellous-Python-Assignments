class Employee:
    def __init__(self, name, sal,dept):
        self.Name = name
        self._Depart = dept
        self.__Sal = sal
    
def main():
    pobj1 = Employee("Vrishabha Pawar", 10000,"Science")
    
if(__name__ == "__main__"):
    main()