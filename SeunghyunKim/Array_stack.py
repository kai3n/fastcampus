class Empty(Exception):
    pass

class ArrayStack:

    def __init__(x):
        x._data = []

    def __len__(x):
        return len(x)
    def is_empty(x):
        if x!=0:
            print("true")
        else:
            print("false")
    def push(x, e):
        x.append(e)
    def top(x):
        return x[len(x)-1]
    def pop(x):
        n = x[len(x)-1]
        del x[len(x)-1]
        return n