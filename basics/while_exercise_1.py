username = None
password = None

while True:
    username = input("create your username:")
    password = input("create your password:")
    if len(username) >= 6 and len(password) >= 8 and username != password:
        break
    else:
        print('try again...')
print("Well done!")