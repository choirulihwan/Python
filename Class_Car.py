class Car:
    def SetType(self, type):
        self._Type = type;
    def GetType(self):
        return self._Type
    def SetModel(self, model):
        self._Model = model
    def GetModel(self):
        return self._Model
    def SetPrice(self, price):
        self._Price = price
    def GetPrice(self):
        return self._Price
    def SetMilesDrive(self, miles):
        self._Miles = miles
    def GetMilesDrive(self):
        return self._Miles
    def SetOwner(self, owner):
        self._Owner = owner
    def GetOwner(self):
        return self._Owner
    def GetCurrentPrice(self):
        return self._Price - (self.GetMilesDrive()*10)


def main():
    myCar = Car()
    myCar.SetType("Toyota")
    myCar.SetModel("Avanza")
    myCar.SetMilesDrive(109000)
    myCar.SetPrice(100000000)
    myCar.SetOwner("Choirul")
    print("The price of MyCar is {}".format(myCar.GetCurrentPrice()))


if __name__ == '__main__': main()
