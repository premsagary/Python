# Multiple Inheritance

class A:
    def hello(self):
        print("AAA")
    def method(self):
        print("1111111")

class B:
    def bye(self):
        print("BBB")
    def method(self):
        print("2222222")


class C(B, A):
    pass

obj_c = C()
obj_c.method()

print(C.__mro__) # Method resolution order


# Changing Inheritance sequence

class C(A, B):
    pass

obj_c = C()
obj_c.method()

print(C.__mro__) # Method resolution order


obj_c.bye()



