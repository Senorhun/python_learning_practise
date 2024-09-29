
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caesar(original_text, shift_amount, encode_or_decode):
        cipher_text = ""
        type = "encoded"
        if encode_or_decode == "decode":
            shift_amount *= -1
            type = "decoded"

        for letter in original_text:
            if letter in abc:
                shifted_index = abc.index(letter) + shift_amount
                shifted_index %= len(abc)
                cipher_text += abc[shifted_index]
            else:
                cipher_text += letter
        print(f"Here is your {type} message: {cipher_text}")
        
while True:
    while True:
        type = input("Do you want to encode or decode?   ")
        if type == "encode" or type == "decode":
            break
        else:
            print("Please choose:")
    text = input(f"text to {type}:  ").lower()
    while True:
        shift_amount = input(f"number to shift letters:  ")
        print(shift_amount)
        if shift_amount.isdigit():
            shift_amount = int(shift_amount)
            break
        else:
            print("Please input a valid number...")
    caesar(text,shift_amount,type)
    run = ""
    while True:
        run = input("Type 'yes' if you want to try again, otherwise type 'no'\n")
        if run == "no" or run == "yes":
            break
        else:
            print("Please choose:")
    if run == "no":
        print("Thank you for en/de-coding with us :)")
        break

