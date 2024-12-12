from consumer import Consumer
from item import Item
from item_type import Item_type
from manager import Manager
import re

class Store:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.user_list = []
        self.item_list = []

    def login_user(self, name, password):
        for user in self.user_list:
            if user.name == name and user.password == password:
                    return True, user.id
        return False, None

    def purchase_item(self, item_id, user_id):
        item = self.find_item_id(item_id)
        user = self.find_user_id(user_id)
        if isinstance(user, Consumer):
            if user.credit >= item.price:
                    if item.available == True:
                        user.credit -= item.price
                        user.purchased_list.append(item)
                        print(f"Purchase successful, new credit: {user.credit}")
                    else:
                        print("Item is not available...")
            else:
                print("Not enough credit...")

    def list_all_item(self):
        for item in self.item_list:
            print(f"id: {item.id},  name: {item.name},  price: {item.price}$, type: {item.type[10:]}, available: {item.available}  ")

    def list_all_user(self, type=""):
        type_mapping = {
        "Consumer": Consumer,
        "Manager": Manager,
        }
        user_type = type_mapping.get(type.capitalize(), None)

        for user in self.user_list:
            if user_type and isinstance(user, user_type):
                if isinstance(user, Consumer):
                  print(f"id: {user.id}, User,  name: {user.name},  credit: {user.credit},  purchased_items: {user.purchased_list}")
                elif isinstance(user, Manager):
                    print(f"id: {user.id}, Manager, name: {user.name},  level: {user.level}")
            elif not user_type:
                if isinstance(user, Consumer):
                  print(f"id: {user.id}, User,  name: {user.name},  credit: {user.credit},  purchased_items: {user.purchased_list}")
                elif isinstance(user, Manager):
                    print(f"id: {user.id}, Manager, name: {user.name},  level: {user.level}")
                    
    def list_item_type(self, type):
        type_upper = str.upper(type)
        print(f"*Items found in type {type_upper}:")
        search_parameter = "Item_type." + type_upper
        for item in self.item_list:
            if item.type == search_parameter:
                print(f"id: {item.id},  name: {item.name},  price: {item.price}$,  available: {item.available}")
    
    def list_user_id(self, id):
        user = self.find_user_id(id)
        if isinstance(user,Consumer):
            purchased_items = ", ".join(str(item) for item in user.purchased_list)
            print(f"id: {user.id}, User,  name: {user.name},  credit: {user.credit},  purchased_items: {purchased_items}")
        elif isinstance(user,Manager):
            print(f"id: {user.id}, Manager, name: {user.name},  level: {user.level}")
    
    def list_item_id(self, id):
        item = self.find_item_id(id)
        print(f"id: {item.id},  name: {item.name},  price: {item.price}$,  available: {item.available}  ")

    def find_item_id(self, id):
        for item in self.item_list:
            if str(item.id) == str(id):
                return item

    def find_user_id(self, id):
        for user in self.user_list:
            if user.id == id:
                return user

    def delete_item(self, id):
        item = self.find_item_id(id)
        self.item_list.remove(item)

    def delete_user(self, id):
        user = self.find_user_id(id)
        self.user_list.remove(user)

    def delete_item(self, id):
        item = self.find_item_id(id)
        self.item_list.remove(item)

    def update_item_price(self, id, price):
        item = self.find_item_id(id)
        if item:
            item.price = price
            print(f"Item successfully updated, new price: {item.price}$")
        else:
            print("No item found")

    def add_item(self, name, price, type):
        type_parameter = "Item_type." + str.upper(type)
        try:
            price = int(price)
            item = Item(name, price, type_parameter)
            self.item_list.append(item)
        except ValueError:
            print(f"Invalid price '{price}' format for item: {name}")
    
    def check_user_name(self, name):
        pattern = r'^[a-zA-Z]+$'
        return bool(re.match(pattern, name))
        
    def add_consumer(self, name, password, credit):
        if self.check_user_name(name):
            consumer = Consumer(name, password, credit)
            self.user_list.append(consumer)
        else:
            print(f"User name '{name}' is not alphabetical..")

    def add_manager(self, name, password, level):
        manager = Manager(name, password, level)
        self.user_list.append(manager)  
          
    def set_item_availability_true(self, id):
        for item in self.item_list:
            if str(id) == str(item.id):
                item.available = True
                break

    def set_item_availability_false(self, id):
        for item in self.item_list:
            if str(id) == str(item.id):
                item.available = False
                break
    
    def add_from_file(self):
        path_r = 'CUBIX/advanced_course/home_work/homework_30/webstore/input.txt'
        with open(path_r, mode='r') as file:
            for line in file:
                line = line.strip()
                if line:
                    item_detail = line.split(',')
                    if len(item_detail) == 3:
                        name, price, type = item_detail[0], item_detail[1], item_detail[2]
                        try:
                            price = int(price)
                            self.add_item(name, price, type)
                        except ValueError:
                            print(f"Invalid price '{price}' format for item: {name}")
                            continue
        print("*input reading finished...")
        
    def list_to_file(self):
        path_w = 'CUBIX/advanced_course/home_work/homework_30/webstore/output.txt'
        result = "\n".join(f"id: {item.id},  name: {item.name},  price: {item.price}$, type: {item.type[10:]}, available: {item.available}" for item in self.item_list)
        with open(path_w, mode='w') as file:
            file.write(result)
            print("output is ready as 'output.txt'")