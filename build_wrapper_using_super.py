class Prem:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def api(self, i):
        return i**2 + self.a + self .b

class Sagar(Prem):
    def api(self, i):
        out = super(Sagar, self). api(i) # Method 1
        # out = Prem.api(self, i)        # Method 2
        return out**2

obj = Sagar(1, 2)
print(obj.api(3))


