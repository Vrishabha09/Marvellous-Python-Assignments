
def DisplayTable(no):
    for i in range(1,11):
        print(no,"x",i,":",no*i)
    print(" ")
    
def main():
    no = int(input("Enter number to print its table : "))
    DisplayTable(no)

if(__name__ == "__main__"):
    main()