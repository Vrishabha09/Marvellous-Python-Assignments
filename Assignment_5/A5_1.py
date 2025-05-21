Addition = lambda no1, no2 : {"Addition":no1 + no2}

Substract = lambda no1, no2 : {"Substraction":no1 - no2}

Multiply = lambda no1, no2 : {"Multiplication":no1 * no2}

Division = lambda no1, no2 : {"Division":no1 / no2}

def My_switch(Task,no1,no2):
   Ans = Task(no1,no2)
   print(Ans)

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    while(no2 < 1):
        print("If you want to perfrom division please enter number greater than '0'.")
        no2 = int(input("Enter second number : "))

    Operations = {1:Addition,2:Substract, 3:Multiply, 4:Division,5:"Exit"}

    Choice = 0
    while(Choice != 5): 
        print("----------------Menu--------------")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        print("----------------------------------")

        Choice = int(input("Enter your choice : "))

        Task = Operations.get(Choice)
        if Task == None:
            print("Please enter valid choice.(1-5)")
            break
        elif((Operations.get(Choice)) == "Exit"):
            print("Thank you!!");
            break
        else:
            My_switch(Task,no1,no2)
            

if(__name__ == "__main__"):
    main()