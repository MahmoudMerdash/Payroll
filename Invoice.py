class Item:
    def __init__(self, description, total_quantity, price_per_one):
        self.description = description
        self.total_quantity = total_quantity
        self.price_per_one = price_per_one
    
    @property
    def price(self):
        return self.price_per_one * self.total_quantity
    


class Invoice:
    def __init__(self, invoice_id):
        self.invoice_id = invoice_id
        self.items = []
        
        
    def add_item(self, item):
        self.items.append(item)
        
    @property
    def amount_to_pay(self):
        return sum([item.price for item in self.items])
    
if __name__ =="__main__":
    i = Item("book",10,50)
    i1 = Item("food",1,500)
    i2 = Item("paper",50,10)
    invoice = Invoice("1250")
    invoice.add_item(i)
    
    invoice.add_item(i1)
    invoice.add_item(i2)
    
    print(invoice.amount_to_pay)
    