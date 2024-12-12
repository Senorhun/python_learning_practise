class User:
    next_id = 0
    def __init__(self, name, password):
        self.name = name
        self.id = User.next_id
        User.next_id += 1
        self.password = password
        

    