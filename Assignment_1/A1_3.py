def Addition(no1,no2):
    ans = 0;
    ans = no1 + no2;
    return ans;

def main():
    no1 = int(input("Enter number to add : "));
    no2 = int(input("Enter number to add : "));

    result = Addition(no1,no2);
    print("Addition of",no1,"and",no2,":",result);

if(__name__ == "__main__"):
    main()