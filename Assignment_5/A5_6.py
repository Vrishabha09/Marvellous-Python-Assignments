# F = (C * 9/5) + 32

CalFahrenhiet = lambda no : (no *(9/5)) + 32

def main():
    no = float(input("Enter temperature in celcius : "))

    Result = CalFahrenhiet(no)

    print("Enter temperature in Fahrenhiet :",Result,"*F")
    
if(__name__ == "__main__"):
    main()