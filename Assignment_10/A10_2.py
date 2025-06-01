
Multiplication = lambda no1,no2 : no1 * no2

def main():
    no1 = int(input("Enter number 1 : "))
    no2 = int(input("Enter number 2 : "))

    result = Multiplication(no1, no2)

    print("Multiplication of",no1,"and",no2,"is :",result)
if(__name__ == "__main__"):
    main()