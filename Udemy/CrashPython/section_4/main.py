class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def __read_speed(self):
        return "speed: "+ str(self.speed) +" km/h"

    def _accelerate(self):
        self.speed += 1
        print(f"{self.brand} going faster, recent {self.__read_speed()}")
    
    def brake(self):
        if self.speed > 0:
            self.speed -= 1
            print(f"{self.brand} going slower: {self.speed}")
        else:
            print(f"{self.brand} cannot slow down...recent {self.__read_speed()}")

car_1 = Car("ship")
car_2 = Car("cart")

if __name__=="__main__":
    car_1._accelerate()
    car_2.brake()
    print(dir(car_1))
    car_1.__read_speed()
    car_1._Car__read_speed()