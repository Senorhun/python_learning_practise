# TODO """
### 1) user_input espresso/latte/cappuccino in loop
### 2) "off" option to end program
### 3) "report" option to print water,milk,coffee,money
### 4) check after user_input if there is sufficient material in machine
### 5) after user_input and check, process money 
### 6) process money value-> if enough proceed, if not terminate, if more give back change, add money to income
### 7) everything fine deduct resources-> create drink
### 8) validations all
# """
# TODO 



def user_input(valid_choice):
    print("*************")
    return input("Terminate program-> off\n" + "Print report-> report" + "\n*************" + "\nWhat would you like to drink?\n" + ", ".join(valid_choice[2:])+ "\n" )

def user_answer(version_a, version_b, version_c):
    user_choice = None
    valid_choice = ["off", "report", version_a, version_b, version_c]
    while user_choice not in valid_choice:
        print("\n"*3 +"Please choose from the list!")
        user_choice = user_input(valid_choice)
    return user_choice

def payment(user_result, container_amount, container_data):
    print("*************")
    print("Insert some coins:")
    while True:
        try:
            quarter = int(input("How many Quarter: "))
            dime = int(input("How many Dime: "))
            nickel = int(input("How many Nickel: "))
            penny = int(input("How many Penny: "))
            print("*************")
            dollar_input = 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny
            if dollar_input < 0:
                raise ValueError
            if dollar_input >= container_data[user_result][3]:
                container_amount["Money"][0] += container_data[user_result][3]
                print(f"Thank you, here is your remaining change ${round(dollar_input-container_data[user_result][3],3)}")
                return True
            else:
                print(f"Sorry, it is not enough for {user_result}, here is your change ${dollar_input}")
                return False
        except ValueError:
            print("Only positive numeric input allowed!")
        
def report(container_amount):
    print("*************")
    for material, amount in container_amount.items():
        if material == "Money":
            print(material + ": " + amount[1] + str(amount[0]))
        else:
            print(material + ": " + str(amount[0]) + amount[1])
    print("*************")

def create(version_selected, container_amount, container_data, user_result):
    if container_amount["Water"][0] >= container_data[version_selected][0]:
        is_enough_water = True
    else:
        is_enough_water = False
    if container_amount["Coffee"][0] >= container_data[version_selected][1]:
        is_enough_coffee = True
    else:
        is_enough_milk = False
    if container_amount["Milk"][0] >= container_data[version_selected][2]:
        is_enough_milk = True
    else:
        is_enough_coffee = False
    if is_enough_water and is_enough_milk and is_enough_coffee:
        container_amount["Water"][0] -= container_data[version_selected][0]
        container_amount["Coffee"][0] -= container_data[version_selected][1]
        container_amount["Milk"][0] -= container_data[version_selected][2]
        if payment(user_result, container_amount, container_data):
            print("Here is your " + version_selected +", enjoy!")
    else:
        refill_list = []
        if not is_enough_water:
            refill_list.append("Water")
        if not is_enough_milk:
            refill_list.append("Milk")
        if not is_enough_coffee:
            refill_list.append("Coffee")
        print("\nRefill is necessary, not enough " + ", " .join(refill_list) +" to make-> " + version_selected)
def turn_off():
    print("Have a nice day, bye!")
    return False

def version_validator(version_list, user_result):
    for version in version_list:
        if version == user_result:
            return version

def main():
    is_on = True
    container_amount = {"Water":[1000, " ml"],"Milk":[1000," ml"],"Coffee":[1000," g"],"Money":[10, " $"]}
    version_a = "espresso"
    version_b = "latte"
    version_c = "cappuccino"
    container_data = {
        "espresso":[100,18,0,1.5],
        "latte":[200,24,150,2.5],
        "cappuccino":[250,24,100,3.0]
        }
    version_list = [version_a, version_b, version_c]
    while is_on:
        user_result = user_answer(version_a, version_b, version_c)
        version_selected = version_validator(version_list, user_result)
        if user_result == "off":
            is_on = turn_off()
        elif user_result == "report":
            report(container_amount)
        elif user_result == version_selected:
           create(version_selected, container_amount, container_data, user_result)

if __name__=="__main__":
    main()