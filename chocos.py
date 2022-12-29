class Chocolate:
    discount_price=5
    def __init__(self,name,flavour,price):
        self.name=name
        self.flavour=flavour
        self.price=price
    def fivestar(self):
        return (self.name+self.flavour)
    def dairymilk(self):
        return (self.name+self.flavour)
    def apply_discount(self):
        self.price=int(self.price-self.discount_price)


