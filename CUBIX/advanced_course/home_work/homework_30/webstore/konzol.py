from store import Store
from manager import Manager
from consumer import Consumer
store = Store("Alza", "Street")

def filter():
    user_input = input("\nWhat would you like to filter?\n'laptop'\n'tv'\n'mobile'\n'tablet'\n'accessory'\n'exit'\n")
    match user_input:
        case "laptop":
            store.list_item_type("laptop")
        case "tv":
            store.list_item_type("tv")
        case "mobile":
            store.list_item_type("mobile")
        case "tablet":
            store.list_item_type("tablet")
        case "accessory":
            store.list_item_type("accessory")

def browse():
    store.list_all_item()

def buy(user_id):
    user_input_item_id = input("Enter item id you wish to buy\n")
    store.purchase_item(user_input_item_id,user_id)

def profile(user_id):
    store.list_user_id(user_id)

def register():
    manager_input_name = input("Enter name of consumer:  \n")
    store.add_consumer(manager_input_name, password="pw", credit = 0)

def add():
    print("\nEnter new item's properties\n")
    user_input_name = input("name:  ")
    user_input_price = input("price:  ")
    user_input_type = input("choose type \n'tv'\n'laptop'\n'tablet'\n'mobile'\n'accessory'\n")
    store.add_item(user_input_name,user_input_price,user_input_type)

def upload():
    store.add_from_file()
    
def download():
    store.list_to_file()

def update():
    user_input_id = input("Enter item's id you wish to update:  ")
    user_input_price = input("Enter item new price:  ")
    store.update_item_price(user_input_id, user_input_price)

def delete():
    user_input_id = input("id of item wish to delete:  ")
    store.delete_item(user_input_id)

def availability():
    user_input_id = input("id of item wish to set:  ")
    user_input = str.capitalize(input("Set 'true' or 'false':  "))
    if user_input == "True":
        store.set_item_availability_true(user_input_id)
        print("Set true successfully..")
    elif user_input == "False":
        store.set_item_availability_false(user_input_id)
        print("Set false successfully..")

def login():
    user_name = input("Enter your name: ")
    user_password = input("Enter your password: ")
    validation, user_id = store.login_user(user_name,user_password)
    user = store.find_user_id(user_id)
    match validation:
        case True:
            if isinstance(user, Consumer):
                consumer_option(user, user_id)
            elif isinstance(user, Manager):
                manager_option(user, user_id)
        case False:
            print("Invalid password...")
        case _:
            print("Invalid option, please try again.\n")
            
def manager_option(user, user_id):
    while True:
        user_input = input(f"\nWelcome Manager {user.name}, what would you like to do?\n'browse'\n'filter'\n'profile'\n'register'\n'add'\n'upload'\n'download'\n'update'\n'delete'\n'availability'\n'exit'\n")
        match user_input:
            case "browse":
                browse()
            case "filter":
                filter()
            case "profile":
                profile(user_id)
            case "register":
                register()
            case "add":
                add()
            case "upload":
                upload()
            case "download":
                download()
            case "update":
                update()
            case "delete":
                delete()
            case "availability":
                availability()
            case "exit":
                break
            case _:
                print("Invalid option, please try again.\n")
     
def consumer_option(user, user_id):
    while True:
        user_input = input(f"\nWelcome Consumer {user.name}, what would you like to do?\n'browse'\n'filter'\n'buy'\n'profile'\n'exit'\n")
        match user_input:
            case "browse":
                browse()
            case "filter":
                filter()
            case "buy":
                buy(user_id)
            case "profile":
                profile(user_id)
            case "exit":
                break
            case _:
                print("Invalid option, please try again.\n")
       
def guest():
    while True:
        user_input = input("\nWhat would you like to do?\n'browse'\n'filter'\n'exit'\n")
        match user_input:
            case "browse":
                browse()
            case "filter":
                filter()
            case "exit":
                break
            case _:
                print("Invalid option, please try again.\n")