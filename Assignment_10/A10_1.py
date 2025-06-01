
Power = lambda no : no**2

def main():
    no = int(input("Enter number to calculate its power to 2 : "))

    result = Power(no)

    print("Square of",no,"is :",result)
if(__name__ == "__main__"):
    main()