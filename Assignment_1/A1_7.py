def ChkDivisible(no):
    if((no % 5) == 0):
        return True;
    else:
        return False;

def main():
    no = int(input("Enter number to check divisibilty by 5: "));
    result = ChkDivisible(no);

    print("Output :",result)

if(__name__ == "__main__"):
    main()