class Product:
    def __init__(self, name, price, deal_price):
        self.name = name
        self.price = price
        self.deal_price = deal_price

    def getProduct(self):
        print("NAME:", self.name)
        print("PRICE:", self.price)
        print("DEAL_PRICE:", self.deal_price)


class Electronics(Product):
    def set_warranty(self, productname, warranty):
        self.productname = productname
        self.warranty = warranty

    def get_warranty(self):
        return self.productname
        return self.warranty


class GrocessaryItems(Product):
    def _init_(self, productdetails, ExpireDate):
        super().__init__(self,productdetails,ExpireDate)
        self.productdetails = productdetails
        self.ExpireDate = ExpireDate

    def grocessarydetails(self):
        super().grocessarydetails()
        print(self.productdetails)
        print(self.ExpireDate)


DetailsObj = Product("Desktop", 500000, 500000)
DetailsObj.getProduct()
electronicObj = Electronics("LAPTOP",30000,30000)
electronicObj.getProduct()
grocessaryObj = Product("dry","AUG 2023" )
grocessaryObj.getProduct()

