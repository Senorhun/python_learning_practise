from book_list import book_list
from library import Library
from member_list import member_list
from member import Member
from konzol import *


new_member_1 = Member("Richard Gray",11)
member_list.append(new_member_1)

library_1.add_book("The Midnight River", "Eliza Storm")
library_1.add_book("Shadows of Tomorrow", "Gregory Nash")
library_1.add_book("Echoes of Eternity", "Mira Lockwood")
library_1.add_book("The Silver Key", "Edgar Wolfe")
library_1.add_book("Winds of the Forgotten", "Isla Carter")
library_1.add_book("The Dark Horizon", "Victor Hale")
library_1.add_book("Fires of the North", "Samantha Drexler")
library_1.add_book("Beneath the Iron Sky", "Lucas Greyson")
library_1.add_book("The Last Ember", "Nina Blackwell")
library_1.add_book("Whispers in the Wind", "Owen Fairchild")


while True:
    user_input = input("\nWelcome to the library, how may I help you?\nsign in as member: 'member'\nbrowse books: 'list'\nprint book list: 'print'\nread book from file: 'read'\nadd book to library: 'add'\nleave library: 'leave'\n")
    match user_input:
        case 'member':
            found_member, id_input = check_member()
            if found_member:
                member(found_member)
            else:   
                print(f"Member id {id_input} not found...")
        case 'read':
            read_book_from_file()
        case 'add':
            add_book()
        case 'print':
            write_list()
        case 'list':
            list_all_book()
        case 'leave':
            print("Thank you for your visit, have a nice day!")
            break
        case _:
            print("Invalid option, please try again.\n")


