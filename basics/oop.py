from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def voice(self):
        pass
    
class Dog(Animal):

    def voice(self):
        return (f"{self.name} doggo says wuff!")

class Cat(Animal):

    def voice(self):
        return (f"{self.name} catso says miauu!")
    
if __name__ == "__main__":
    dog1 = Dog("Bono", 3)
    print(dog1.voice())

    cat1 = Cat("Sir Mici", 1)
    print(cat1.voice())
    