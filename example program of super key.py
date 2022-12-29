class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
    def display_product_details(self):
        print("Product:",self.name)
        print("Price:",self.price)
        print("Deal_price:",self.deal_price)kh
        print("Rating:",self.ratings)
    def get_deal_price(self):
        return self.deal_price
class ElectronicItem(Product):
    def set_warranty(self,warranty_in_months):
        self.warranty_in_months=warranty_in_months
    def get_warranty(self):
        return self.warranty_in_months
class GrocessaryItem(Product):
    def __init__ (self,name,price,deal_price,ratings,expiry_date,package_date):
        super().__init__(name,price,deal_price,ratings)
        self.expiry_date=expiry_date
        self.package_date=package_date
    def display_product_details(self):
        super().display_product_details()
        print("Expiry date:",self.expiry_date)
        print("Package Date:",self.package_date)


productObj=Product("Milk" , 10 , 9 , 5)
productObj.display_product_details()
print("===================================================")
electronicObj=ElectronicItem("IPhone",10,9,5)
electronicObj.display_product_details()
print("================================================")
g=GrocessaryItem("Dal",20,10,5,2022,88)
g.display_product_details()




