class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(f"Selling price is {self.__maxprice}")
    def updatemax(self , price):
        self.__maxprice=price

a=computer()
a.sell()


#Changing the price of private variable

a.__maxprice=1000
a.sell()


#Using the updatemax fuction inside the class

a.updatemax(1000)
a.sell()

