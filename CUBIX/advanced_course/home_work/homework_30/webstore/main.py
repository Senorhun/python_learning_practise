from item import Item
from item_type import Item_type
from manager import Manager
from consumer import Consumer
from konzol import *

store.add_consumer("Bono","000",0)
store.add_consumer("Jubo","111",200)
store.add_manager("Juno", "222","junior")
store.add_item("Asus 345D","10", "TV")
store.add_item("Sony bigLama","5", "LAPTOP")
store.set_item_availability_true(0)

while True:
    user_input = input("\nWelcome to our webshop!\nWould you like to log in? 'yes' or 'no'\nLeaving the store enter 'exit'\n")
    match user_input:
        case "yes":
            login()
        case "no":
            guest()
        case "exit":
            print("\nThank you for visiting our store, have a nice day!")
            break
        case _:
            print("Invalid option, please try again...\n")


