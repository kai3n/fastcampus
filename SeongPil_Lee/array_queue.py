class Empty(Exception):
    pass

class ArrayQueue:

    def __init__(self):
        self._data = [None]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def first(self):
        if self.is_empty() == True :
            print('Error')
        else:
            return self._data[0]

    def dequeue(self):
        if self.is_empty() == True:
            print('Error')
        else:
            a = self.first()
            self._data = self._data[1:]
            return a

    def enqueue(self, e):
        self._data.append(e)

s = ArrayQueue()

s.enqueue(2)
s.enqueue(3)
s.enqueue(6)

s.dequeue()
print(s._data)