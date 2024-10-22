def greetings(name = None):
    if name is None:
        print("Hello, world!")
    else:
        print(f"Hello, {name}!")
    
greetings("Peter")
greetings()