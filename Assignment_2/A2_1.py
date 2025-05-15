import Arithmetic as Ar

def My_SwitchCase(choice,no1,no2):
    if(choice == 1):
        ans = Ar.Add(no1,no2)
        print("Addition is :",ans);
    elif(choice == 2):
        ans = Ar.Sub(no1,no2)
        print("Substraction is :",ans);
    elif(choice == 3):
        ans = Ar.Mult(no1,no2)
        print("Multiplication is :",ans);
    elif(choice == 4):
        ans = Ar.Div(no1,no2)
        print("Division :",ans);

def main():
    no1 = int(input("Enter one number : "))
    no2 = int(input("Enter one number : "))

    choice = -1;

    while(choice != 5):
        print("--------------Arithmetic Operations----------------")
        print("1. Addition");
        print("2. Subtract");
        print("3. Multiply");
        print("4. Divide");
        print("5. Exit")
        print("---------------------------------------------------")
        choice = int(input("Enter your choice : "))

        if(choice == 5):
            print("Thank you!!");
            break
        elif(choice > 5):
            print("Enter proper choice.");
            break
        else:
            My_SwitchCase(choice,no1,no2);


if(__name__ == "__main__"):
    main();