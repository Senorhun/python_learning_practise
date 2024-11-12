starting main automatically add:
- 10 dummy books to library
- 1 dummy member to library

to sign in as member use id -> dummy member_name: "Richard Gray", id: 11
to sign in as librarian member use code -> librarian_code = 123

Usage and functions:
- main (start file)
- program welcomes as a non-member first:
    - sign in as a member to access more options
    - browse book list (terminal)
    - print book list into file (output.txt)
    - add book via reading from file (input.txt)
    - add book manually (title, author)
    - leave program

- sign in using id to access member options:
    - sign in as a librarian to access more options
    - profile (name, id, borrowed books)
    - borrow book by title
    - return book by title
    - previous options from non-member

- sign in using id to access librarian options:
    - register new member by name (id automatic)
    - update member by id (name, id)
    - remove member by id (yes/no)
    - delete book by title (yes/no)
    - list unavailable books (borrowed)
    - previous options from non-member

Structure
- main.py display the options for non-member
- konzol.py contains more options for member and librarian
    - cleancode match-case one-liner functions
- library.py contains logic for functions