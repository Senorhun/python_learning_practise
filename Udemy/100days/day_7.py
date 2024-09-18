
from random import choice


ascii_list = [
    """
6 lives left
------
|    |
|    
|    
|    
|    
|
--------

    """,
    """
    5 lives left
------
|    |
|    O
|    
|    
|    
|
--------
    """,
    """
4 lives left
------
|    |
|    O
|    |
|    
|    
|
--------
    """,
    """
3 lives left
------
|    |
|    O
|   /|
|    
|    
|
--------
    """,
    """
2 lives left
------
|    |
|    O
|   /|\\
|    
|    
|
--------
    """,
    """
1 lives left
------
|    |
|    O
|   /|\\
|   / 
|    
|
--------
    """,
    """
0 lives left
------
|    |
|    O
|   /|\\
|   / \\
|    
|
--------
    """
]


word_list = ["work", "fun", "happy"]

word = choice(word_list)
letter_list = []

life = 6
while True:

    guess = ""
    letter = input("Letter:  ")
    if letter in letter_list:
        print("****Already guessed that!****")
    hit = False
    for let in word:
        if let == letter:
            guess += letter
            letter_list.append(letter)
            hit = True
        elif let in letter_list:
            guess += let
        else:
            guess += "_"
    if not hit:
        life -= 1
        print("****Nope, you have lost a life...****")
    print(guess)
    if "_" not in guess:
        print("****Congrats u won!****")
        break
    elif life == 6:
        print(ascii_list[0])
    elif life == 5:
        print(ascii_list[1])
    elif life == 4:
        print(ascii_list[2])
    elif life == 3:
        print(ascii_list[3])
    elif life == 2:
        print(ascii_list[4])
    elif life == 1:
        print(ascii_list[5])
    elif life == 0:
        print(ascii_list[6])
        print(f"****Sorry, you lost...Solution was -> {word}****")
        break


