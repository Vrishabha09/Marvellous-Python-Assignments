class BankAccount:
    ROI = 10.5

    def __init__(self,n,a):
        self.Name = n
        self.Amount = a

    def Deposit(self,credit):
        self.Amount += credit 
        print("Balance :",self.Amount)

    def Withdraw(self,debit):
        if debit > self.Amount:
            print("Insufficient funds.")
            print("Balance :",self.Amount)
        else:
            self.Amount -= debit
            print("Balance :",self.Amount)

    def CalculateInterest(self,years):
        Ans = (self.Amount * BankAccount.ROI * years)/100
        print("Simple interest for",years,"year's':",Ans)

    def Display(self):
        print("Name :",self.Name,"Balance :",self.Amount)

def main():
    bobj = BankAccount("Vrishabha Pawar", 100000)
    bobj1 = BankAccount("Sarthak Pawar",200000)
    bobj2 = BankAccount("Shubham Pawar",300000)
    bobj3 = BankAccount("Shivtej Pawar",4000)

    bobj.Deposit(1001)
    bobj.Withdraw(50000)
    bobj.Display()
    bobj.CalculateInterest(1)

    bobj1.Deposit(200)
    bobj1.Withdraw(10000)
    bobj1.Display()
    bobj1.CalculateInterest(2)

    bobj2.Deposit(112)
    bobj2.Withdraw(350000)
    bobj2.Display()
    bobj2.CalculateInterest(3)

    bobj3.Deposit(20001)
    bobj3.Withdraw(5000)
    bobj3.Display()
    bobj3.CalculateInterest(5)

if(__name__ == "__main__"):
    main()