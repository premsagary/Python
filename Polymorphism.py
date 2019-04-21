"""
Polymorphism is the ability to leverage the same interface for different underlying forms such as data types or classes

"""

print(12 + 13)

print("edureka" + "rocks")

print([1, 2] + [3, 4])

#  Same Interface but different underlying forms


# Prem
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

# Sudiptha
class Cat(Animal):
    def talk(self):
        print("Meowwwww")

# Fred
class Dog(Animal):
    def talk(self):
        print("Woof")


################# Client/ User ###############

c = Cat("Kitty")
print(c.talk())

d = Dog("Tommy")
print(d.talk())