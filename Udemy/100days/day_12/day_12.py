# prim catcher

def is_prim(num):
    prim = False
    num_list = [2,3,4,5,6,7,8,9]
    result = [number for number in num_list if num % number == 0]
    if len(result) <= 1:
        prim = True
    return prim

print(is_prim(7))

print("-----------")

enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside: {enemies}")

increase_enemies()
print(f"enemies outside: {enemies}")

print("-----------")

enemies = 1
def increase_enemies():
    return enemies + 1

print(increase_enemies())
print(f"enemies outside: {enemies}")
enemies = increase_enemies()
print(f"enemies outside: {enemies}")