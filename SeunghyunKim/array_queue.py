class Empty:
    def error(arr):
        if(len(arr)==0):
            print("error")

class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self._front = 0

    def __len__(self):
        return len(self)

    def is_empty(self):
        if self!=0:
            return False
        else:
            return True

    def first(self):
        if len(self) == 0:
            raise Empty.error(self)
        else:
            return self[0]

    def dequeue(self):
        if len(self) == 0:
            raise Empty.error(self)
        else:
            n = self[0]
            del self[0]
            return n

    def enqueue(self, x):
        self.append(x)