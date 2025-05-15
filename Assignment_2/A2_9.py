def CntDigits(no):
    cnt = 0
    temp = -1
    while(temp != 0):
        temp = int(no/10)
        no = temp
        cnt += 1
    return cnt

def main():
    no = int(input("Enter number: "))
    result = CntDigits(no);
    print("Count of digits :",result);

if(__name__ == "__main__"):
    main()