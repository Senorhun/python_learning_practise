from item_type import Item_type

class Item:

    next_id = 0
    def __init__(self, name, price, type: Item_type):
        self.name = name
        self.id = Item.next_id
        Item.next_id += 1
        self.price = price
        self.available = False
        self.type = type

    
    def __str__(self):
        return f"Item(id:{self.id}, name:{self.name}, price:{self.price}$)"
