from user import User

class Consumer(User):

    def __init__(self, name, password, credit):
        super().__init__(name, password)
        self.credit = credit
        self.purchased_list = []