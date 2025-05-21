
def CheckEligibility(age):
    if age >= 18:
        return True
    else:
        return False
    
def main():
    age = int(input("Enter Age : "))
    Result = CheckEligibility(age)
    if Result:
        print("You are eligble to vote.");
    else:
        print("You are not eligble to vote.");

if(__name__ == "__main__"):
    main()