class Animal():
    def __init__(self, age, num_of_leg):
        self.age = age
        self.num_of_leg = num_of_leg
    
    def ageing(self, ageing_year):
        self.age += ageing_year
    def introduce(self):
        return f"{self.age} years old {self.num_of_leg} legged "
    
class Pet(Animal):
    def __init__(self, name, age, num_of_leg):
        super().__init__(age, num_of_leg)
        self.name = name
    
    def introduce(self):
        return f"{self.name}, who is a " + super().introduce() + "pet"
    
class Dog(Pet):
    def __init__(self, name, age, num_of_leg):
        super().__init__(name, age, num_of_leg)
    def introduce(self):
        return "It is a dog named " +super().introduce()

class Spider(Animal):
    def __init__(self, age, num_of_leg):
        super().__init__(age, num_of_leg)
    
    def introduce(self):
        return "It is a " + super().introduce() + "spider"

pet1 = Pet("Bob", 2, 3)
print(pet1.introduce())
pet1.ageing(1)
print(pet1.introduce())

dog1 = Dog("Morzsi", 3, 4)
print(dog1.introduce())
dog1.ageing(1)
print(dog1.introduce())

spider1 = Spider(3, 4)
print(spider1.introduce())
spider1.ageing(1)
print(spider1.introduce())