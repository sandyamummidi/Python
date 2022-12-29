class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
    def display_product_details(self):
        print("Product:",self.name)
        print("Price:",self.price)
        print("Deal_price:",self.deal_price)
        print("Rating:",self.ratings)
    def get_deal_price(self):
        return self.deal_price
class ElectronicItem(Product):
    def set_warranty(self,warranty_in_months):
        self.warranty_in_months=warranty_in_months
    def get_warranty(self):
        return self.warranty_in_months
class GrocessaryItem(Product):
    pass
class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity",quantity)
    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill+=price
            print("Total Bill:",total_bill)


milk=GrocessaryItem("Milk",40,25,3.5)
tv=ElectronicItem("TV",45000,40000,3.5)
order=Order("Prime Delivery","Hyderabad")
order.add_item(milk,2)
order.add_item(tv,1)
print("++++++++++")
order.display_order_details()
print("++++++++++")
order.display_total_bill()