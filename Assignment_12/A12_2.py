class Circle:

    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self,r):
        self.Radius = r

    def CalculateArea(self):
        self.Area = self.PI*(self.Radius*self.Radius)

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Radius :",self.Radius,"Area :",self.Area,"Circumference :",self.Circumference)

def main():
    cobj1 = Circle()
    cobj2 = Circle()

    cobj1.Accept(10)
    cobj1.CalculateArea()
    cobj1.CalculateCircumference()
    cobj1.Display()

    cobj2.Accept(5)
    cobj2.CalculateArea()
    cobj2.CalculateCircumference()
    cobj2.Display()

if(__name__ == "__main__"):
    main()