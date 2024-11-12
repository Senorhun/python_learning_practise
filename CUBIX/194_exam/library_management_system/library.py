from book import Book
from book_list import book_list
from member_list import member_list
from member import Member

class Library:

    def __init__(self, name, book_list, member_list):
        self.name = name
        self.book_list = book_list
        self.member_list = member_list
        self.librarian_code = "123"
    
    def list_book(self):
        print("\nHere you can find the list of our books:")
        print("***************")
        for book in book_list:
            if book.is_borrowed == False:
                print(f"title: {book.title}, author: {book.author}")
        print("***************")

    def list_book_unavailable(self):
        print("\nHere you can find the list of our borrowed books:")
        print("***************")
        for book in book_list:
            if book.is_borrowed == True:
                print(f"title: {book.title}, author: {book.author}")
        print("***************")

    def check_member_id(self, member_id):
        for member in member_list:
            if member.id == member_id:
               return member

    def check_book_title(self,book_title):
        for book in book_list:
            if book.title == book_title:
                return book

    def check_librarian_code(self, member_id):
        found_member = self.check_member_id(member_id)
        if found_member:
            input_code = input("\nPlease type librarian code: ")
            if input_code == self.librarian_code:
                return True
            else:
                print(f"Access denied to {found_member.name} (wrong password)")
        
    def librarian_member_register(self, new_member_name):
        new_member_id = max(member.id for member in self.member_list) + 1
        new_member = Member(new_member_name ,new_member_id)
        member_list.append(new_member)
        print(f"New member {new_member_name} with id({new_member_id}) is registered!")

    def librarian_member_update(self, member_id):
        found_user = self.check_member_id(member_id)
        if found_user:
            self.profile(member_id)
            librarian_input = input("What would you like to change: 'name' or 'id'\n")
            match librarian_input:
                case 'name':
                    previous_name = found_user.name
                    librarian_input_name = input(f"Type how to change {previous_name}'s name: ")
                    found_user.name = librarian_input_name
                    print(f"Name is updated from {previous_name} to {found_user.name}")
                case 'id':
                    previous_id = found_user.id
                    librarian_input_id = int(input(f"Type how to change {found_user.name}'s id({found_user.id}): "))
                    found_user.id = librarian_input_id
                    print(f"Id is updated from {previous_id} to {found_user.id}")
        else:
            print(f"No user was found with id: {member_id}")
    def librarian_member_remove(self, member_id):
        found_member = self.check_member_id(member_id)
        if found_member:
            print(f"\nname: {found_member.name} id: {found_member.id}")
            librarian_input_remove = input(f"Are you sure to remove? 'yes' or 'no'\n")
            if librarian_input_remove == "yes":
                self.member_list.remove(found_member)
                print("Member is removed")
        else:
            print(f"Member id {member_id} not found...")

    def librarian_book_delete(self, book_title):
        found_book = self.check_book_title(book_title)
        if found_book:
            print(f"\nname: {found_book.title} author: {found_book.author}")
            librarian_input_remove = input(f"Are you sure to remove? 'yes' or 'no'\n")
            if librarian_input_remove == "yes":
                self.book_list.remove(found_book)
                print("Book is removed")
        else:
            print(f"Book name {book_title} not found...")

    def profile(self,member_id):
        found_member = self.check_member_id(member_id)
        if found_member:
            print(f"\nname: {found_member.name} id: {found_member.id}")
            if len(found_member.borrowed_books) == 0:
                print("No borrowed book.")
            else:
                print("__Borrowed books__")
                for book in found_member.borrowed_books:
                    print(f"title: {book.title} author: {book.author}")
        else:
            print(f"Member id {member_id} not found...")
            
    def borrow_book(self, member_id, book_title):
        found_member = self.check_member_id(member_id)
        if found_member:        
            found_book = self.check_book_title(book_title)
            if found_book:
                if found_book.is_borrowed:
                    print(f"*Sorry {found_member.name}, the book named {found_book.title} is borrowed right now...")
                else:
                    found_book.is_borrowed = True
                    print(f"*Book '{book_title}' added to {found_member.name}'s borrowed books list.")
                    print(f"*{book_title} is now borrowed. Enjoy!")
                    found_member.borrowed_books.append(found_book)

            else:
                print(f"*Sorry, book not found with title: {book_title}")
        else:
            print(f"*Member with ID {member_id} not found.")

    
    def return_book(self, member_id, book_title):
        found_member = self.check_member_id(member_id)
        if found_member:        
            found_book = self.check_book_title(book_title)
            if found_book:
                if found_book.is_borrowed:
                    found_member.borrowed_books.remove(found_book)
                    found_book.is_borrowed = False
                    print(f"*Thank you {found_member.name}, the book named {found_book.title} is returned.")
                elif found_book not in found_member.borrowed_books:
                    print(f"You do not have the book named {found_book.title} borrowed")

            else:
                print(f"*Sorry, book not found with title: {book_title}")
        else:
            print(f"*Member with ID {member_id} not found.")


    def add_book(self,book_title, book_author):
        number_of_books = len(book_list)
        for book in self.book_list:
            if book.title == book_title:
                print(f"Already have {book.title} thx anyway...")
                return
        new_book = Book(book_title, book_author)
        self.book_list.append(new_book)
        updated_number_of_books = len(book_list)
        if updated_number_of_books > number_of_books:
            print("Thank you for your kindness!")
            print(f"New book added with title: {book_title} author: {book_author}")
        