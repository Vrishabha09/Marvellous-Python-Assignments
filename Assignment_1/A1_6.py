def ChkNum(no):
    if(no > 0):
        print("Positive");
    elif(no < 0):
        print("Negative");
    elif(no == 0):
        print("Zero");
def main():
    no = int(input("Enter number : "));
    ChkNum(no);

if(__name__ == "__main__"):
    main()