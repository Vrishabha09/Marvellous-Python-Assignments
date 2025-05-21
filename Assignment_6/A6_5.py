
def is_Prime(no): 
    ans = True
    for i in range(2,int(no/2)+1):
        if no % i == 0:
            ans = False
            break
    return ans

def main():
    no = int(input("Enter number to check if its prime : "))
    if no == 1 or no == 2:
        print("Number is Prime")
    else:
        result = is_Prime(no)
        print(result)
        if result:
            print("Number is prime")
        else:
            print("Number is not prime")

    
if(__name__ == "__main__"):
    main()