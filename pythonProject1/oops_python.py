class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")


my_car = Car("Toyota", "Camry", 2022)
my_car.start_engine()


# //////////////////////////////////////////////
# Encapsulation
class Car:
    def __init__(self, make, model, year):
        self._make = make  # protected attribute
        self.__model = model  # private attribute
        self.year = year

    def start_engine(self):
        print("Engine started")


my_car = Car("Toyota", "Camry", 2022)
print(my_car._make)  # accessing protected attribute
# print(my_car.__model)  # error: accessing private attribute

# ////////////////////////////////////////////////////
# Inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.num_wheels = 4
        print("car inherits its property from vehicle class")

my_car = Car("Toyota", "Camry", 2022)
my_car.start_engine()
# //////////////////////////////////////////////
# Polymorphisam
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

my_animals = [Animal(), Dog(), Cat()]
for animal in my_animals:
    animal.speak()

# ///////////////////////////
# Abstartion
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

my_shape = Rectangle(10, 5)
print(my_shape.area())



