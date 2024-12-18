#home_work_1-1
while True:
    question = input("What is the answer to the Great question?  ")
    if question == "42":
        print("Yes, indeed it is, well done!")
        break
    else:
        print("You have a long way to go, youngling...try again!")


#home_work_1-2
first_name = input("Input your First name please: ")
if first_name == "":
    first_name = "John"
sur_name = input("Input your Surname please: ")
if sur_name == "":
    sur_name = "Doe"
print(f"Welcome to the Batcave, Master {first_name} {sur_name} !")