def CntDigits(no):
    sum = 0
    temp = -1
    while(temp != 0):
        sum = sum + int(no%10)
        temp = int(no/10)
        no = temp
    return sum

def main():
    no = int(input("Enter number: "))
    result = CntDigits(no);
    print("Sum of digits :",result);

if(__name__ == "__main__"):
    main()