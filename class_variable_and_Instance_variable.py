""" Class variables can be accessed via  class name or object, but it can modified only by class name """



class Edureka:
    a = "class variable"

    def __init__(self, n ):
        self.name = n
        self.dept = "Data science"



print(Edureka.a)

obj = Edureka ("Ravi")
print(obj.a)

""" Modify class variable """

Edureka.a = "new value"

print(Edureka.a)
print(obj.a)
print(obj.dept)


#######


obj1 = Edureka("prem")
print(Edureka.a)
print(obj1.a)


obj2 = Edureka("sagar")
print(Edureka.a)
print(obj2.a)

########

obj3 = Edureka("Ravi")
obj4 = Edureka("Ram")

print(obj3.name)
print(obj4.name)
print(obj3.dept)
print(obj4.dept)
