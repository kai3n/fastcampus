class Empty(Exception):
    pass

class ArrayQueue:

    def __init__(self):
        self._data = []


    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data):
            return False
        else:
            return True


    def first(self):
        if len(self._data) == False:
            raise Empty("error")
        else:
            return self._data[0]

    def dequeue(self):
        val = self._data[0]
        del self._data[0]
        return val


    def enqueue(self, e):
        self._data.append(e)


Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(3)
print(len(Q))
print(Q.dequeue())
print(len(Q))
print(Q.first())

