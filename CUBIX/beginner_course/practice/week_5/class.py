class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def ageing(self, ageing_year):
        self.age += ageing_year
    def introduce(self):
        return f"{self.name} {self.age},"
    
animal1 = Animal("xyz", 3)

class Dog(Animal):
    def introduce(self):
        return super().introduce() +  f" Vau, I am {self.name} and {self.age} years old"
class Bird(Animal):
    def introduce(self):
        return f" Chirp, I am {self.name} and {self.age} years old"


print(animal1.introduce())
animal1.ageing(2)
print(animal1.introduce())

dog1 = Dog("Morzsi", 2)
print(dog1.introduce())
dog1.ageing(2)
print(dog1.introduce())

bird1 = Bird("Cip", 1)
print(bird1.introduce())
bird1.ageing(2)
print(bird1.introduce())

