class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price

s1=computer()
s1.sell()
s1.__maxprice=1000
s1.sell()
s1.setmaxprice(2000)
s1.sell()