
def DisplayEvenSum(no):
    Sum = 0
    for i in range(0,no+1,2):
        Sum += i
    return Sum

def main():
    Sum = DisplayEvenSum(100)
    print("Sum of all even numbers from 1 - 100 :",Sum)
if(__name__ == "__main__"):
    main()