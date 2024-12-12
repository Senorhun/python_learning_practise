from user import User

class Manager(User):

    def __init__(self, name, password, level):
        super().__init__(name, password)
        self.level = level
