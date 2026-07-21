class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
    def make_sound(self):
        print(f"{self.name} is making a sound.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")
    def make_sound(self):
        print(f"{self.name} says Woof")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")
    def make_sound(self):
        print(f"{self.name} says Meow")
    
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

dog.eat()
dog.sleep()
dog.bark()
dog.make_sound()
cat.eat()
cat.sleep()
cat.meow()
cat.make_sound()