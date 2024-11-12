from member import Member

class Librarian(Member):

    def __init__(self, name, id, code):
        super().__init__(name, id)
        self.code = code
        