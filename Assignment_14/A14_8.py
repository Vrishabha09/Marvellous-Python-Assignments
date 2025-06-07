
class Vehicle:
    def __init__(self):
        print("Inside Vehicle constructor")

    def Start(self):
        print("Start the vehicle")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Inside Car constructor")

    def Start(self):
        print("Start the Car")

def main():
    vobj = Vehicle()
    vobj.Start()  

    cobj = Car()
    cobj.Start()  
if(__name__ == "__main__"):
    main()