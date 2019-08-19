class Car:
    def __init__(self, **kwargs):
        self._Data = kwargs
        if (self._Data.get("type")):
            self._Type = self._Data["type"]
        if (self._Data.get("model")):
            self._Model = self._Data["model"]
        if (self._Data.get("price")):
            self._Price = self._Data["price"]
        if (self._Data.get("miles")):
            self._Miles = self._Data["miles"]
        if (self._Data.get("owner")):
            self._Owner = self._Data["owner"]

    def GetCurrentPrice(self):
        if (self._Data.get("price")) and (self._Data.get("miles")):
            return self._Price - (self._Miles*10)


def main():
    myCar = Car(type="Toyota", model="Fortuner", price=40000, miles=10, owner="Choirul")
    print("The price of {} Car is {}".format(myCar._Owner, myCar.GetCurrentPrice()))
    myCar2 = Car(type="Honda", price=20000, miles=5, owner="Erna")
    print("The price of {} Car is {}".format(myCar2._Owner, myCar2.GetCurrentPrice()))
    myCar3 = Car(model="Expander", owner="Daffa", type="Mitsubishi")
    print("The price of {} Car is {}".format(myCar3._Owner, myCar3.GetCurrentPrice()))


if __name__ == '__main__': main()
