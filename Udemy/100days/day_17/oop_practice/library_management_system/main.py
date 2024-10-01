from book_list import book_list
from library import Library
from member_list import member_list
from member import Member

library_1 = Library("Central Library", book_list, member_list)

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

for book in library_1.book_list:
    print(f"title: {book.title}, author: {book.author}")


print("---")

for i, member in enumerate(member_list, start = 1):
    if i == 11:
        break
    if i < 10:
        # new_member_id = "00" + str(i)
        new_member_name = "new_member_00" + str(i)
    elif i >= 10:
        # new_member_id = "0" + str(i)
        new_member_name = "new_member_0" + str(i)
    new_member = Member(new_member_name ,i)
    member_list.append(new_member)

for member in member_list:
    print(f"name: {member.name} id: {member.id} books: {member.borrowed_books}")

print("---")

while True:
    try:
        user_input = input("\nWelcome to the library, how may I help you?\nsign in as member: 'member\nbrowse books: 'list'\nadd book to library: 'add'\nleave library: 'leave'\n")
        match user_input:
            case 'member':
                id_input = int(input("Please type member id: "))
                found_member = library_1.check_member_id(id_input)
                if found_member:
                    is_online = True
                    while is_online:
                        try:
                            user_input_member = input(f"\nWelcome to the library {found_member.name}, how may I help you?\nlibrarian system: 'librarian'\nview profile: 'profile'\nadd book to library: 'add'\nborrow book from library: 'borrow'\nreturn book to library: 'return'\nlist available books: 'list'\nleave library: 'leave'\n")
                            match user_input_member:
                                case 'librarian':
                                    if library_1.check_librarian_code(found_member.id):
                                        while True:
                                            try:
                                                user_input_librarian = input(f"\nWelcome librarian {found_member.name}, how may I assist you?\nregister new member: 'register'\nupdate member: 'update'\nremove member: 'remove\ndelete book: 'delete'\nlist available books: 'list'\nlist unavailable books: 'unlisted'\nsign out as librarian: 'leave'\n")
                                                match user_input_librarian:
                                                    case 'register':
                                                        member_name = input("Please type member's name: ")
                                                        library_1.librarian_member_register(member_name)
                                                        for member in member_list:
                                                            print(f"name: {member.name} id: {member.id} books: {member.borrowed_books}")
                                                    case 'update':
                                                        librarian_input = int(input(f"Please type member id to change: "))
                                                        library_1.librarian_member_update(librarian_input)
                                                    case 'remove':
                                                        librarian_input = int(input(f"Please type member id to remove: "))
                                                        library_1.librarian_member_remove(librarian_input)
                                                    case 'add':
                                                        author_input = input("Please type author's name: ")
                                                        title_input = input("Please type title: ")
                                                        library_1.add_book(title_input,author_input)
                                                    case 'delete':
                                                        librarian_input = input(f"Please type book title to remove: ")
                                                        library_1.librarian_book_delete(librarian_input)
                                                    case 'list':
                                                        library_1.list_book()
                                                    case 'unlisted':
                                                        library_1.list_book_unavailable()
                                                    case 'leave':   
                                                        print("Thank you for your work, have a nice day!")
                                                        is_online = False
                                                        break
                                                    case _:
                                                        print("Invalid option, please try again.\n")
                                            except ValueError:
                                                print("Please use digits for id!")                               
                                case 'profile':
                                    library_1.profile(found_member.id)
                                case 'add':
                                    author_input = input("Please type author's name: ")
                                    title_input = input("Please type title: ")
                                    library_1.add_book(title_input,author_input)
                                case 'borrow':
                                    library_1.list_book()
                                    title_input = input("Please type title: ")
                                    library_1.borrow_book(found_member.id, title_input)
                                case 'return':
                                    title_input = input("Please type title: ")
                                    library_1.return_book(found_member.id, title_input)
                                case 'list':
                                    library_1.list_book()
                                case 'leave':
                                    print("Thank you for your visit, have a nice day!")
                                    is_online = False
                                case _:
                                    print("Invalid option, please try again.\n")
                        except ValueError:
                            print("Please use digits for id!")
                else:   
                    print(f"Member id {id_input} not found...")
            case 'add':
                author_input = input("Please type author's name: ")
                title_input = input("Please type title: ")
                library_1.add_book(title_input,author_input)
            case 'list':
                library_1.list_book()
            case 'leave':
                print("Thank you for your visit, have a nice day!")
                break
            case _:
                print("Invalid option, please try again.\n")
    except ValueError:
        print("Please use digits for id!")

