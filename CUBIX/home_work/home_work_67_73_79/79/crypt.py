code_list = [ 
    ("A", "X"),    ("B", "Y"),  ("C", "Z"),  ("D", "W"),   ("E", "V"),
    ("F", "U"),    ("G", "T"),  ("H", "S"),  ("I", "R"),   ("J", "Q"),
    ("K", "P"),    ("L", "O"),  ("M", "N"),  ("N", "M"),   ("O", "L"),
    ("P", "K"),    ("Q", "J"),  ("R", "I"),  ("S", "H"),   ("T", "G"),
    ("U", "F"),    ("V", "E"),  ("W", "D"),  ("X", "C"),   ("Y", "B"),
    ("Z", "A"),    ("0", "9"),  ("1", "8"),  ("2", "7"),   ("3", "6"),
    ("4", "5"),    ("5", "4"),  ("6", "3"),  ("7", "2"),   ("8", "1"),
    ("9", "0"),    
]

code_dict = dict(code_list)
decode_dict = {code[1] : code[0] for code in code_list}

def encrypt(text):
    result = ""
    for char in text:
        if char in code_dict:
            result += code_dict[char]
            result += " "
        else:
            result += char
    return result.strip()

def decrypt(coded):
    result = ""
    for code in coded.split(" "):
        result += decode_dict[code]
    return result

text_to_encrypt = "hello world"
encrypted = encrypt(text_to_encrypt.upper())
print(encrypted)

text_to_decrypt = "S V O O L D L I O W"
decrypted = decrypt(text_to_decrypt.upper())
print(decrypted)