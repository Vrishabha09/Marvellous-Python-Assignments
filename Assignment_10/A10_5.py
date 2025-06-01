
class FMRTasks:
    def __init__(self):
        self.Ans = False

    def Prime(self,no):
        
        if(no == 1) or (no == 2):
            return True
        else:
            for i in range(2,no):
                if(no%i) == 0:
                    return False
                else:
                    Ans = True

        return Ans
    
    def Multiply(self,no):
        return no*2
    
    def Max(self,Max,no):
        if(Max < no):
            Max = no
        
        return Max


class FMR:
    def __init__(self):
        self.FData = list()
        self.MData = list()
        self.RData = 0

    def FilterX(self,Task,iList):
        for data in iList:
            ans = Task(data)
            if(ans):
                self.FData.append(data)

        return self.FData
    
    def MapX(self,Task,FData):
        for data in FData:
            ans = Task(data)
            self.MData.append(ans)

        return self.MData

    def ReduceX(self,Task,MData):
        Add = 0
        for data in MData:
            self.RData = Task(Add,data)

        return self.RData
    
def main():
    iList = list()
    no = int(input("Enter number of elements in list : "))

    for i in range(no):
        data = int(input(f"Enter element {i+1}: "))
        iList.append(data)

    print("Original list :",iList)

    fobj = FMR()
    tobj = FMRTasks();

    FData = list(fobj.FilterX(tobj.Prime,iList))
    print("Filtered list :",FData)

    MData = list(fobj.MapX(tobj.Multiply,FData))
    print("Mapped data :",MData)

    RData = fobj.ReduceX(tobj.Max,MData)
    print("Reduced Data :",RData)
    
if(__name__ == "__main__"):
    main()