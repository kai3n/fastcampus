class Empty(Exception):
    pass

class ArrayQueue:

    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) is 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            result = self._data[0]
            self._data = self._data[1:]
            return result


    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]

a = ArrayQueue()


a.enqueue(3)
a.enqueue(5)
print(a._data)

print(len(a))

print(a.dequeue())
print(a.dequeue())

print(a._data)

a.enqueue(8)
a.enqueue(9)
a.enqueue(10)

print(a._data)

print(a.first())
print(a.dequeue())
print(a._data)