#3. Billing System for Retail Store Scan products, apply discounts,
#  generate bills, and record transactions.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class BillingSystem:
    def __init__(self):
        self.cart = []

    def add_product(self, name, price):
        product = Product(name, price)
        self.cart.append(product)

    def generate_bill(self, discount=0):
        total = sum(p.price for p in self.cart)
        total = total - (total * discount / 100)

        print("----- BILL -----")
        for p in self.cart:
            print(p.name, p.price)

        print("Total after discount:", total)