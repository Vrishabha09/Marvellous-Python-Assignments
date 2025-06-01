Cnt = 0

def DisplayCount(no):
    global Cnt
    if no > 0:
        Temp = no % 10
        if Temp == 0:
            Cnt += 1
            
        DisplayCount(int(no/10))
    
    return Cnt

def main():
    no = int(input("Enter number : "))
    Ret = DisplayCount(no)

    print("Zeroes :",Ret)
if(__name__ == "__main__"):
    main()