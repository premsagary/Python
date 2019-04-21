class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hello(self):
        print("AAA")

class B(A):
    def __init__(self, c, d):
        self.c = c
        self.d = d

print(B.__mro__)

# b = B(1, 2) # when you do this 1, 2 are assigned to c, d
# b.a  # this will result in error "AttributeError: 'B' object has no attribute 'a'"
# Super is used to call parent class method


class B(A):
    def __init__(self, c, d):
        super(B, self).__init__(10, 20)  # call parent class syntax 1
        # A.__init__(self, c+10, d+10)   # call parent class synatx 2
        # super().__init__(10, 20)       # call parent class syntax 3
        self.c = c
        self.d = d

b = B(1, 2)
print(b.a)

