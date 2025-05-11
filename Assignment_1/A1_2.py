def ChkNum(no):
    if((no % 2) == 0):
        print("Even number");
    else:
        print("Odd nnumber");

def main():
    no = int(input("Enter number to check odd/even : "));
    ChkNum(no);

if(__name__ == "__main__"):
    main()