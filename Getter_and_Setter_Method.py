"""
NOT IMPORTANT

"""


class Edureka:
    def __init__(self, courseName):
        self.courseName = courseName

    def getter_courseName(self):
        return self.courseName

    def setter_courseName(self):
        self.courseName = new_val


object = Edureka("Python")
print(object.getter_courseName())

object.courseName = "new value"   # Bad Practice
object.setter_courseName("new_value")

object = Edureka("Python")
print(object.setter_courseName())