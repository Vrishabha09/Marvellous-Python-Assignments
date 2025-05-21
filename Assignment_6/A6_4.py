def Factorial(no):
    Fact = 1 
    for i in range(1,no+1):
        Fact *= i
    return Fact
def main():
    no = int(input("Enter number to print its factorial : "))
    result = Factorial(no)
    print("Factorial of",no,"is :",result)

if(__name__ == "__main__"):
    main()