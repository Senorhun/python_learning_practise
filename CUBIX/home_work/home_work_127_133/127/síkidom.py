from abc import ABC, abstractmethod

class Síkidom(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def periphery(self):
        pass


class Téglalap(Síkidom):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b
    
    def periphery(self):
        return 2 * (self.a + self.b)


class Négyzet(Téglalap):
    def __init__(self, a):
        super().__init__(a, a)


class Kör(Síkidom):
    PI = 3.141592

    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.r ** 2 * Kör.PI
    
    def periphery(self):
        return 2 * self.r * Kör.PI


class Test(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass


class Téglatest(Test):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def volume(self):
        return self.a * self.b * self.c
    
    def surface_area(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)


class Kocka(Téglatest):
    def __init__(self, a):
        super().__init__(a, a, a)


class Gömb(Test):
    PI = 3.141592

    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4 / 3) * Gömb.PI * (self.r ** 3)

    def surface_area(self):
        return 4 * Gömb.PI * (self.r ** 2)


téglalap = Téglalap(3, 4)
print(f"Téglalap területe: {téglalap.area()}")
print(f"Téglalap kerülete: {téglalap.periphery()}")

négyzet = Négyzet(3)
print(f"Négyzet területe: {négyzet.area()}")
print(f"Négyzet kerülete: {négyzet.periphery()}")

téglatest = Téglatest(3, 4, 5)
print(f"Téglatest térfogata: {téglatest.volume()}")
print(f"Téglatest felszíne: {téglatest.surface_area()}")

kocka = Kocka(3)
print(f"Kocka térfogata: {kocka.volume()}")
print(f"Kocka felszíne: {kocka.surface_area()}")

gömb = Gömb(3)
print(f"Gömb térfogata: {round(gömb.volume(),2)}")
print(f"Gömb felszíne: {round(gömb.surface_area(),2)}")
