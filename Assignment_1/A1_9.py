def DisplayEven(no1):
    cnt = 0
    i = 1
    while(cnt != no1):
        if((i %2) == 0):
            print(i,end=" ");
            i = i + 1
            cnt = cnt + 1
        else:
            i = i + 1

def main():
    no1 = int(input("Enter number to print even number : "));
    
    DisplayEven(no1);

if(__name__ == "__main__"):
    main()