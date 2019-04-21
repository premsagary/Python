# Multi-level inheritance

class Animal:
    def eat(self):
        print("Eating......")

class Dog(Animal):
    def bark(self):
        print("barking......")

class Puppy(Dog):
    def weep(self):
        print("Weeping......")


d = Puppy()
d.eat()
d.bark()
d.weep()




