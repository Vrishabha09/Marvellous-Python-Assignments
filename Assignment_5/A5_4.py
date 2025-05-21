def main():
    print("Enter 3 numbers to check maximum")
    no1 = int(input("Enter number : "))
    no2 = int(input("Enter number : "))
    no3 = int(input("Enter number : "))

    if(no1 > no2):
        if(no1 > no3):
            print("Largest number is :",no1)
        elif(no3 > no2):
            print("Largest number is :",no3)
    elif(no2 > no3):
        print("Largest number is :",no2)
    else:
        print("Largest number is :",no3)
if(__name__ == "__main__"):
    main()