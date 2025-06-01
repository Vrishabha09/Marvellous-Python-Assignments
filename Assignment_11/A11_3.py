Sum = 0

def SumDigit(no):
    global Sum
    if no > 0:
        Temp = no%10
        Sum += Temp
        SumDigit(int(no/10))
     
    return Sum

def main():
    no = int(input("Enter number : "))
    ret = SumDigit(no)
    print("Sum of digits :",ret)
if(__name__ == "__main__"):
    main()