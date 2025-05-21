
ChkEven = lambda no : no % 2

def main():
    no = int(input("Enter number : "))

    Ans = ChkEven(no)
    
    if Ans == 0:
        print("Even")
    else:
        print("Odd")

if(__name__ == "__main__"):
    main()