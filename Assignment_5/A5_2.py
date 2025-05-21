
def CheckVowel(c):
    char = c.lower()
    
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return True
    else:
        return False
    
def main():
    char = input("Enter a character : ")
    Result = CheckVowel(char)
    if Result:
        print("'",char,"' is a vowel.");
    else:
        print("'",char,"' is not a vowel.");

if(__name__ == "__main__"):
    main()