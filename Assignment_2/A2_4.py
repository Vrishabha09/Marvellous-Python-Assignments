#  User defined
def Factors(no):
    sumFactors = 0;
    for i in range(1,int((no/2)+1),1):
        if((no % i) == 0):
            sumFactors = sumFactors + i
    return sumFactors

# def Factors2(no,i = 1):
#     if i > no:
#         return 0
#     if no % i == 0:
#         return i + Factors2(no, i + 1)
#     else:
#         return Factors2(no, i + 1)
    
# Factor3 = lambda no,i=1 :  (i + Factor3(no, i+1)) if (no % i == 0) else Factor3(no,i+1)

def main():
    no = int(input("Enter number : "))
    result = Factors(no)
    print("Addition of factors of",no,"is :",result);

if(__name__ == "__main__"):
    main();