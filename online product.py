class Product:
    def __init__(self,name,price,deal_price):
        self.name=name
        self.price=price
        self.deal_price=deal_price
    def getProduct(self):
         print("NAME:",self.name)
         print("PRICE:",self.price)
         print("DEAL_PRICE:",self.deal_price)
class Electronics:
    def __init__(self,productname,warranty):
        self.productname=productname
        self.warranty=warranty

    def getwarranty(self):
        print(self.productname)
        print(self.warranty)

class GrocessaryItems:
    def __init__(self,productdetails,ExpireDate):
        self.productdetails=productdetails
        self.ExpireDate=ExpireDate

    def grocessarydetails(self):
        print(self.productdetails)
        print(self.ExpireDate)

DetailsObj=Product("Desktop",500000,500000)
DetailsObj.getProduct()



