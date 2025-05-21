def ChkPallindrome(string):
    temp = ""

    for i in range(len(string)-1,-1,-1):
        temp += string[i]
    
    if temp == string:
        return True
    else:
        return False

def main():
    string = input("Enter string to check if pallindrome : ")
    ans = ChkPallindrome(string)

    if ans:
        print(string," is pallindrome")
    else:
        print(string,"is not pallindrome")
if(__name__ == "__main__"):
    main()