class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        if len(self) == 0:
            return True
        else :
            return False

    def push(self, e):
        self.data.append(e)


    def top(self):
        return self.data[len(self.data)-1]

    def pop(self):
        if len(self) == 0:
            print("error")
        else:
            a = self.data[len(self.data)-1]
            del(self.data[len(self.data)-1])
            return a



s = ArrayStack()
print(s.push(5))
print(s.push(3))
print(len(s))
print(s.pop())
print(s.data)
print(s.is_empty())
print(s.pop())
print(s.is_empty())
print(s.push(7))
print(s.data)
print(s.push(9))
print(s.top())
print(s.push(4))
print(len(s))
print(s.pop())