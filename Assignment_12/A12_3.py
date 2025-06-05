
class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self,no1,no2):
        self.Value1 = no1
        self.Value2 = no2

    def Addition(self):
        Ans = 0
        Ans = self.Value1 + self.Value2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.Value1 - self.Value2
        return Ans
    
    def Multiplication(self):
        Ans = 0
        Ans = self.Value1 * self.Value2
        return Ans
    
    def Division(self):
        Ans = 0
        try:
            Ans = self.Value1 / self.Value2
        except ZeroDivisionError as zobj:
            print("Division by zero not allowed")
        return Ans

def main():
    Aobj1 = Arithmetic()
    Aobj1.Accept(13,10)
    Add = Aobj1.Addition()
    Sub = Aobj1.Substraction()
    Mult = Aobj1.Multiplication()
    Div = Aobj1.Division()

    print("Addition : ",Add,"Substraction : ",Sub,"Multiplication : ",Mult,"Division : ",Div)

    Aobj2 = Arithmetic()
    Aobj2.Accept(3,0)
    Add = Aobj2.Addition()
    Sub = Aobj2.Substraction()
    Mult = Aobj2.Multiplication()
    Div = Aobj2.Division()

    print("Addition : ",Add,"Substraction : ",Sub,"Multiplication : ",Mult,"Division : ",Div)

if(__name__ == "__main__"):
    main()