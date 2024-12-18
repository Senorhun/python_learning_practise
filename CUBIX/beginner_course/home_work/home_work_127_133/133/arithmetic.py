class Arithmetic:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Arithmetic):
            return Arithmetic(self.value + other.value)
        return Arithmetic(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Arithmetic):
            return Arithmetic(self.value - other.value)
        return Arithmetic(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Arithmetic):
            return Arithmetic(self.value * other.value)
        return Arithmetic(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Arithmetic):
            return Arithmetic(self.value / other.value)
        return Arithmetic(self.value / other)

    def __str__(self):
        return f'Arithmetic result is ({self.value})'

a = Arithmetic(3)
b = Arithmetic(5)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(b * "q")
