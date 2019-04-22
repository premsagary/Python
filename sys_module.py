import sys

age = eval(input("enter your age:"))
if not isinstance(age, int):
    print("Age is not a number")
    sys.exit(-1)
if age >= 18:
    print("vote")
else:
    print("Come back later")
    print(sys.version)
    print(help('modules'))
    print(sys.prefix)
