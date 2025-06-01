Sum = 0

def DisplaySum(no):
    global Sum
    if no > 0:
        Sum += no
        DisplaySum(no-1)
    
    return Sum

def main():
    no = int(input("Enter number : "))
    Ret = DisplaySum(no)

    print("Sum of 1 -",no,":",Ret)
if(__name__ == "__main__"):
    main()