class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        print ("length is",len(self._data))

    def is_empty(self):
        if(len(self._data) == 0):
            return True
        return False

    def push(self, e):
        self._data.append(e)

    def top(self):
        print(self._data[len(self._data)-1])

    def pop(self):
        if(len(self._data) == 0):
            print ("error")

        else:
            last_index = len(self._data)-1
            print (self._data[last_index])
            del (self._data[last_index])


s = ArrayStack()
s.push(5)
s.push(3)
s.__len__()
s.pop()
print(s.is_empty())
s.pop()
print(s.is_empty())
s.pop()
s.push(7)
s.push(9)
s.top()
s.push(4)
s.__len__()
s.pop()
s.push(6)
s.push(8)
s.pop()

print("hello")