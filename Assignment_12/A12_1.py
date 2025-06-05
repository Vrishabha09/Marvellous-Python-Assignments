class Demo:

    Value = "Demo Claas"

    def __init__(self,no1,no2):
        self.iNo1 = no1
        self.iNo2 = no2

    def Fun(self):
        print("Value from fun :",self.iNo1)

    def Gun(self):
        print("Value from gun :",self.iNo2)
def main():
    obj1 = Demo(10,13)
    obj2 = Demo(23,4)

    obj1.Fun()
    obj2.Gun()

if(__name__ == "__main__"):
    main()