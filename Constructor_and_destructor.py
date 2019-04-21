class Edureka:
    def __init__(self):
        print("111")

    def __del__(self):
        print("object is going to be deleted, used for cleanup actions")

obj = Edureka()
del obj
print("#"*10)