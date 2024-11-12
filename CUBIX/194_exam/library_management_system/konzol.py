from book_list import book_list
from library import Library
from member_list import member_list

library_1 = Library("Central Library", book_list, member_list)

def member(found_member):
    is_online = True
    while is_online:
            user_input_member = input(f"\nWelcome to the library {found_member.name}, how may I help you?\nlibrarian system: 'librarian'\nview profile: 'profile'\nprint book list: 'print'\nread book from file: 'read'\nadd book to library: 'add'\nborrow book from library: 'borrow'\nreturn book to library: 'return'\nlist available books: 'list'\nleave library: 'leave'\n")
            match user_input_member:
                case 'librarian':
                    login_librarian(found_member)                              
                case 'profile':
                    check_profile(found_member)
                case 'add':
                    add_book()
                case 'read':
                    read_book_from_file()
                case 'print':
                    write_list()
                case 'borrow':
                    borrow_book(found_member)
                case 'return':
                    return_book(found_member)
                case 'list':
                    list_all_book()
                case 'leave':
                    print("Thank you for your visit, have a nice day!")
                    is_online = False
                case _:
                    print("Invalid option, please try again.\n")

def librarian(found_member):
    while True:
        try:
            user_input_librarian = input(f"\nWelcome librarian {found_member.name}, how may I assist you?\nregister new member: 'register'\nupdate member: 'update'\nremove member: 'remove\ndelete book: 'delete'\nprint book list: 'print'\nread book from file: 'read'\nlist available books: 'list'\nlist unavailable books: 'unlisted'\nsign out as librarian: 'leave'\n")
            match user_input_librarian:
                case 'register':
                    register_member()
                case 'update':
                    update_member()
                case 'remove':
                    remove_member()
                case 'add':
                    add_book()
                case 'read':
                    read_book_from_file()
                case 'print':
                    write_list()
                case 'delete':
                    delete_book()
                case 'list':
                    list_all_book()
                case 'unlisted':
                    list_all_unavailable_book()
                case 'leave':   
                    print("Thank you for your work, have a nice day!")
                    is_online = False
                    break
                case _:
                    print("Invalid option, please try again.\n")
        except ValueError:
            print("Please use digits for id!")  

def write_list():
    path_w = 'CUBIX/194_exam/library_management_system/output.txt'
    result = "\n".join(f"{book.title} by {book.author}" for book in library_1.book_list)
    with open(path_w, mode='w') as file:
        file.write(result)
        print("output is ready as 'output.txt'")

def read_book_from_file():
    path_r = 'CUBIX/194_exam/library_management_system/input.txt'
    with open(path_r, mode='r') as file:
        for line in file:
            line = line.strip()
            if line:
                book_detail = line.split(',')
                if len(book_detail) >= 2:
                    title, author = book_detail[0], book_detail[1]
                    library_1.add_book(title, author)
    print("input reading finished...")

def check_member():
    found_member = None
    id_input = None
    try:
        id_input = int(input("Please type member id: "))
    except ValueError:
            print("Please use digits for id!")
    found_member = library_1.check_member_id(id_input)
    return found_member, id_input

def add_book():
    author_input = input("Please type author's name: ")
    title_input = input("Please type title: ")
    library_1.add_book(title_input,author_input)

def list_all_book():
    library_1.list_book()

def return_book(found_member):
    title_input = input("Please type title: ")
    library_1.return_book(found_member.id, title_input)

def borrow_book(found_member):
    library_1.list_book()
    title_input = input("Please type title: ")
    library_1.borrow_book(found_member.id, title_input)
    
def login_librarian(found_member):
        if library_1.check_librarian_code(found_member.id):
            librarian(found_member)

def check_profile(found_member):
    library_1.profile(found_member.id)

def register_member():
    member_name = input("Please type member's name: ")
    library_1.librarian_member_register(member_name)
    for member in member_list:
        burrowed_books = [book.title for book in member.borrowed_books]
        print(f"name: {member.name} id: {member.id} books: {burrowed_books}")

def update_member():
    librarian_input = int(input(f"Please type member id to change: "))
    library_1.librarian_member_update(librarian_input)

def remove_member():
    librarian_input = int(input(f"Please type member id to remove: "))
    library_1.librarian_member_remove(librarian_input)

def delete_book():
    librarian_input = input(f"Please type book title to remove: ")
    library_1.librarian_book_delete(librarian_input)

def list_all_unavailable_book():
    library_1.list_book_unavailable()

