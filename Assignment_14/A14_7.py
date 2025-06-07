
class Person:
    def __init__(self,n,a):
        self.Name = n
        self.Age = a
        
class Teacher(Person):
    def __init__(self, n, a, sub, sal):
        self.Subject = sub
        self.Sal = sal
        super().__init__(n, a)

    def Display(self):
        print("Name :",self.Name)
        print("Age :",self.Age)
        print("Subject :",self.Subject)
        print("Salary :",self.Sal)

def main():
    pobj = Teacher("Vrishabha Pawar",23,"Java",250000)
    pobj.Display()

    pobj2 = Teacher("Shubham Pawar",19,"Maths",350000)
    pobj2.Display()
if(__name__ == "__main__"):
    main()