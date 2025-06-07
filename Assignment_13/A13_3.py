
class Arithmetic:
    def __init__(self,v):
        self.Value = v

    def ChkPrime(self):
        if(self.Value <= 2):
            return True
        else:
            for i in range(2,int(self.Value/2)):
                if self.Value % i == 0:
                    return False
        return True
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1,int(self.Value)):
            if self.Value % i == 0:
                sum += i
        
        if sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors of ",self.Value,":",end=" ")
        for i in range(1,int(self.Value)):
            if self.Value % i == 0:
                print(i,"|",end=" ")
        print("")

    def SumFactors(self):
        sum = 0
        for i in range(1,int(self.Value)):
            if self.Value % i == 0:
                sum += i

        return sum
    
def main():
    cobj1 = Arithmetic(12)
    cobj2 = Arithmetic(11)
    cobj3 = Arithmetic(28)
    cobj4 = Arithmetic(50)

    print("------------------------Object 1----------------------------")
    ret = "Number is Prime" if cobj1.ChkPrime() else "Number is not prime"
    print(ret)
    ret = "Number is Perfect" if cobj1.ChkPerfect() else "Number is not perfect"
    print(ret)
    cobj1.Factors()
    ret = cobj1.SumFactors()
    print("Sum of factors :",ret)

    print("------------------------Object 2----------------------------")
    ret = "Number is Prime" if cobj2.ChkPrime() else "Number is not prime"
    print(ret)
    ret = "Number is Perfect" if cobj2.ChkPerfect() else "Number is not perfect"
    print(ret)
    cobj2.Factors()
    ret = cobj2.SumFactors()
    print("Sum of factors :",ret)

    print("------------------------Object 3----------------------------")
    ret = "Number is Prime" if cobj3.ChkPrime() else "Number is not prime"
    print(ret)
    ret = "Number is Perfect" if cobj3.ChkPerfect() else "Number is not perfect"
    print(ret)
    cobj3.Factors()
    ret = cobj3.SumFactors()
    print("Sum of factors :",ret)

    print("------------------------Object 4----------------------------")
    ret = "Number is Prime" if cobj4.ChkPrime() else "Number is not prime"
    print(ret)
    ret = "Number is Perfect" if cobj4.ChkPerfect() else "Number is not perfect"
    print(ret)
    cobj4.Factors()
    ret = cobj4.SumFactors()
    print("Sum of factors :",ret)



if(__name__ == "__main__"):
    main()