#Encapsulation
class Bank():
    def __init__(self,amount):
        self.__amount=amount
    def Withdraw(self,remove):
        self.tesaii=remove
        self.__amount-=remove
        print(self.__amount)

__amount=0
bank=Bank(1000)
bank.Withdraw(700)

#super()
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

student = Student("Alice", 123)
print(student.name)
print(student.roll)

#Polymorphism
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"  

class Cat(Animal):
    def make_sound(self):
        return "Meow"   

dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())

#Abstraction
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

rectangle = Rectangle(5, 10)
print(rectangle.area())

#Method Overriding
class Vehicle:
    def start(self):
        print("Vehicle is starting.")  

class Car(Vehicle):
    def start(self):
        print("Car is starting.")

car = Car()
car.start()

#Runtime Polymorphism
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
cat = Cat()
animals=[dog, cat]
for animal in animals:
    print(animal.make_sound())
