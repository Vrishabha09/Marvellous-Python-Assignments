def Display(no1,name):
    for i in range(no1,name): 
        print(name);         

def main():
    name = input("Enter name you want to print : ");
    no1 = int(input("Enter number to print : "));
    
    Display(no1,name); 

if(__name__ == "__main__"):
    main()