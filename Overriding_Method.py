class Parent:
    def method1(self):
        print("call method Parent")

class Child(Parent):
    def method1(self):
        print("call method Child")


object = Child()
print(object.method1())

# It will call Child

# If both classes use init, you need to use super


