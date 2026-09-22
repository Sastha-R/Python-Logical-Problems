class bank:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def printfun(self):
        print(self.brand,self.model,self.price)



obj = bank("porsche","911","30000000")
obj.printfun()

obj2 = bank("porsche","911 GTR","300000000")
obj2.printfun()

obj3 = bank("porsche","911 GTR 3","350000000")
obj3.printfun()
        