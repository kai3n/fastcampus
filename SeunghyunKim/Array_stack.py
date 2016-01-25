class Empty:
    def error(x):
        if(len(x)==0):
            print("error")

class ArrayStack:

    def __init__(x):
        x._data = []

    def __len__(x):
        return len(x)
    def is_empty(x):
        if x!=0:
            return True
        else:
            return False
    def push(x, e):
        x.append(e)
    def top(x):
        return x[len(x)-1]
    def pop(x):
        if len(x) == 0:
            raise Empty.error(x)
        else:
            n = x[len(x)-1]
            del x[len(x)-1]
            return n