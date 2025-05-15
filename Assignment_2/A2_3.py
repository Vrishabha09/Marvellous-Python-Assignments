#   Using Built in module 
# import math
# def factorial(n):
#     return(math.factorial(n))

#   Using user-defined module
# def Factorial(no):
#     fact = 1
#     for i in range(1,no+1,1):
#         fact = fact * i
#     return fact

#   Using recursion
# def Factorial(no):
#     return 1 if(no == 1 or no == 0) else no*Factorial(no-1)

Factorial = lambda no : 1 if(no == 1 or no == 0) else no*Factorial(no-1)

def main():
    no = int(input("Enter number to calculate its factorial : "))

    result = Factorial(no)
    print("Factorial of",no,"is :",result);

if(__name__ == "__main__"):
    main()    