
class NegativeDimensionError(Exception):
    pass

class Rectangle:
    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise NegativeDimensionError(f"Dimensions cannot be negative: a={a}, b={b}")
        self.a = a
        self.b = b
def check_for_valid_rectangle(a, b):
    try:
        rectangle = Rectangle(a,b)
        match rectangle:
            case Rectangle(a=x, b=y) if x == y:
                return f"valid Square with a={x}"
            case Rectangle(a=x, b=y):
                return f"valid Rectangle with a={x} and b={y}"
    except NegativeDimensionError as e:
        return str(e)

if __name__ == "__main__":
    print("***" + check_for_valid_rectangle(a = 1, b = 2))
    print("***" + check_for_valid_rectangle(a = 1, b = 1))
    print("***" + check_for_valid_rectangle(a = -1, b = 2))
    print("***" + check_for_valid_rectangle(a = 3, b = 7))

