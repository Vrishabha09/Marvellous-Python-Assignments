
class Rectangle:
    def __init__(self,l,b):
        self.Len = l
        self.Bredth = b
    
    def Area(self):
        Ans = 0
        Ans = self.Len * self.Bredth
        print("Area :",Ans)

    def Perimeter(self):
        Ans = 0
        Ans = 2*(self.Len + self.Bredth)
        print("Perimeter :",Ans)

def main():
    robj = Rectangle(10,5)
    robj.Area()
    robj.Perimeter()
if(__name__ == "__main__"):
    main()