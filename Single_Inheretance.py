"""
Super = Base = Parent
Sub = Derived = Child

"""


# Single

class Vehicle:
    def __init__(self, a, b, c):
        self.brand = a
        self.color = b
        self.no_of_tyres = c
        self._pro = 100
        self.__pri = 200

    def apply_brake(self):
        # some logic for applying brake
        print("Brakes applied")

class Car(Vehicle):
    pass

Car_obj = Car("honda", 'black', 4)
print(Car_obj.brand)
print(Car_obj.color)
print(Car_obj.no_of_tyres)
print(Car_obj.apply_brake())
print(Car_obj._pro)

# Namemangling
# print(Car_obj.__pri) #Cannot access the private variable like this from the parent class
print(Car_obj._Vehicle__pri)  #you should access like this