
class BankAccount:
    def __init__(self,n,b,Ac):
        self.AccountNo = Ac
        self.Name = n
        self.Bal = b

    def Deposit(self,credit):
        self.Bal += credit

    def Withdraw(self,debit):
        if self.Bal < debit:
            print("Insufficient Balance.")
            print("Pro tip -> Abhyas Kar bhikari.")
        else:
            self.Bal -= debit
            print("Amount '",debit,"'withdrawn successfully.")
            print("Current Balance :",self.Bal)
    
    def DisplayBal(self):
        print("Balance :",self.Bal)

def main():
    bobj = BankAccount("Vrishabha Pawar",10000,4370001239)
    bobj.DisplayBal()
    bobj.Deposit(510)
    bobj.DisplayBal()
    bobj.Withdraw(5000)
    bobj.DisplayBal()
    bobj.Withdraw(20000)
    bobj.DisplayBal()
if(__name__ == "__main__"):
    main()