morse_code_list = [
    ("A", ".-"),    ("B", "-..."),  ("C", "-.-."),  ("D", "-.."),   ("E", "."),
    ("F", "..-."),  ("G", "--."),   ("H", "...."),  ("I", ".."),    ("J", ".---"),
    ("K", "-.-"),   ("L", ".-.."),  ("M", "--"),    ("N", "-."),    ("O", "---"),
    ("P", ".--."),  ("Q", "--.-"),  ("R", ".-."),   ("S", "..."),   ("T", "-"),
    ("U", "..-"),   ("V", "...-"),  ("W", ".--"),   ("X", "-..-"),  ("Y", "-.--"),
    ("Z", "--.."),  ("0", "-----"), ("1", ".----"), ("2", "..---"), ("3", "...--"),
    ("4", "....-"), ("5", "....."), ("6", "-...."), ("7", "--..."), ("8", "---.."),
    ("9", "----."), (" ", " ")
]
morse_code_dict = dict(morse_code_list)
morse_decode_dict = {morse_code[1] : morse_code[0] for morse_code in morse_code_list}

def encrypt(text):
    result = ""
    for char in text:
        result += morse_code_dict[char]
        result += " "
    return result.strip()

def decrypt(coded):
    result = ""
    for code in coded.split(" "):
        result += morse_decode_dict[code]
    return result

text_to_encrypt = "hello world"
encrypted = encrypt(text_to_encrypt.upper())
print(encrypted)

text_to_decrypt = ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
decrypted = decrypt(text_to_decrypt.upper())
print(decrypted)