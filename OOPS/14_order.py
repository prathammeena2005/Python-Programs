class Order:
    def __init__(self, item, price):
        self.item=item
        self.price=price

    def __gt__(self, odr2):
        if self.price>odr2.price:
            return True
        else:
            return False
    
odr1=Order("Chips",20)
odr2=Order("Pen", 10)
print(odr1>odr2)
