class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self,prev):
        if isinstance(prev, Product):
            return self.price == prev.price
        return False

    #def __repr__(self):
        #return f"Product(name='{self.name}', price={self.price})"
    
def main():
    pobj1 = Product("Laptop", 1000)
    pobj2 = Product("Smartphone", 1000)
    pobj3 = Product("Super Car", 1000000)

    if pobj1 == pobj2:
        print("Prices of Laptop and Smartphone is same")
    else:
        print("Prices of Laptop and Smartphone is not same")

    if pobj2 == pobj3:
        print("Prices of Super Car and Smartphone is same")
    else:
        print("Prices of Super Car and Smartphone is not same")
if(__name__ == "__main__"):
    main()