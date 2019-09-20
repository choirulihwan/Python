class Car:
    def __init__(self, type, model, price, miles, owner):
        self._Type = type
        self._Model = model
        self._Price = price
        self._Miles = miles
        self._Owner = owner

    def GetCurrentPrice(self):
        return self._Price - (self._Miles*10)


def main():
    myCar = Car("Toyota", "Avanza", 100000000, 109000, "Choirul")
    print("The price of MyCar is {}".format(myCar.GetCurrentPrice()))


if __name__ == '__main__': main()
