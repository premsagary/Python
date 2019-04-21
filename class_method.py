# Example 1:

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod  # cls = Date
    def dmy(cls, day, month, year):
        return Date(year, month, day)

    @classmethod
    def mdy(cls, month, day, year):
        return Date(year, month, day)

a = Date(2018, 2, 21)
b_obj = a.dmy(22, 3, 2018)
print(b_obj.year)
print(b_obj.month)
print(b_obj.day)


print("#"*20)

# Example 2:

class Mycalss:
    i = 200
    def __init__(self, m, n):
        self.m = m
        self.n = n

    @classmethod
    def hello(cls, a, b):
        print(cls.i)
        print(a, b)
        # print(self.m)  # Not allowed in class method



obj = Mycalss(100, 200)
print(Mycalss)
Mycalss.hello(1, 2)


