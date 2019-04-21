"""
NOT IMPORTANT

"""


class Edureka:
    def __init__(self, courseName):
        self.courseName = courseName

    def getter_courseName(self):
        return self.courseName

    def setter_courseName(self, new_val):
        self.new_val = new_val


object = Edureka("Python")
print(object.getter_courseName())

object.courseName = "new value"   # Bad Practice
print(object.setter_courseName())

object1 = Edureka("Python")
print(object1.setter_courseName())