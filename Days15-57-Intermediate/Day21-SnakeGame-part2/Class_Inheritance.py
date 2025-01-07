# Inheritance
# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

emo = Fish()
emo.breathe()

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")
        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")
        
class Nemo(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Nemo created")

    def whoAmI(self):
        print("Nemo")

    def swim(self):
        print("Swimming")


print("\n")

d = Dog()
d.whoAmI()
d.eat()
d.bark()

print("\n")

n = Nemo()
n.whoAmI()
n.eat()
n.swim()

print("\n")

a = Animal()
a.whoAmI()
a.eat()