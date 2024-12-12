About my Webstore program:
A simple terminal application where manager can handle storage,
and consumer able to browse and buy items. There are options 
to handle bigger shipments using read from file or to output 
all the items into a file. Watch out for File reader pathways
in order to work properly in store.py line 144 and 161.

starting main automatically add:
- 2 dummy consumer and 1 manager to store user_list
- 2 dummy item store item_list, id: 0 set availability True (buyable)

to sign in as consumer use name "Bono", password: 000
    - credit: 0 unable to buy items
to sign in as consumer use name "Jubo", password: 111
    - credit: 200 able to buy items
to sign in as manager use name "Juno", password: 222

Usage and functions:
- main (start file)
- program welcomes as a non-member first:
    - log in
    - browse or filter by type (Enum)
    - exit program

- log in as consumer using name and password:
    - all non member options
    - profile (id, designation, name, credit, purchased items)
    - buy (if enough credit)
    - log out

- log in as manager using name and password:
    - all non member options
    - register new member by name (id, password, credit are automatic)
    - CRUD items
    - log out

Structure
- main.py display the main options
- konzol.py contains options for consumer and manager
    - cleancode match-case 
    - one-liner functions used from store.py
- store.py contains general logic for functions