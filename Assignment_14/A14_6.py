
class Calculator:
    def __init__(self,no1,no2):
        self.iNo1 = no1
        self.iNo2 = no2

    def Addition(self):
        print("Addition :",self.iNo1 + self.iNo2)
    
    def Subtract(self):
        print("Substraction :",self.iNo1 - self.iNo2)
    
    def Multiply(self):
        print("Multiplication :",self.iNo1 * self.iNo2)
    
    def Divide(self):
        Ans = 0.0 
        try:
            Ans = self.iNo1 / self.iNo2
            print("Division :",Ans)
        except ZeroDivisionError as zobj:
            print("Error : Cant perform division with Zero.")

def main():
    iNo1 = int(input("Enter first number : "))
    iNo2 = int(input("Enter second number : "))

    Choice = -1

    cobj = Calculator(iNo1,iNo2)
    Operations = {1:cobj.Addition,2:cobj.Subtract,3:cobj.Multiply,4:cobj.Divide,5:"Exit"}

    while(Choice != 5):
        print("----------------Calculator operation--------------")
        print("1.Addition.\n2.Subtract.\n3.Multiply.\n4.Divide.\n5.Exit")
        print("--------------------------------------------------")
        Choice = int(input("Enter a choice : "))

        #Task = Operations[Choice]
        Task = Operations.get(Choice)
        if Task == None:
            print("Please enter valid choice.(1-5)")
            continue
        elif((Operations.get(Choice)) == "Exit"):
            print("Thank you!!");
            break
        else:
            Task()
                          
if(__name__ == "__main__"):
    main()