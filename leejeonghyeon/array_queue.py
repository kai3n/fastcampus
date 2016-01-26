class Empty(Exception):
    pass

class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        #return len(self._data) is 0 만 해도 된다
        if len(self._data) <= 0:
            return True
        else:
            return False

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            f_num = self._data[0]
            del self._data[0]
        return f_num
        """
        else:
            result = self._data[0]
            self._data = self._data[1:]
            return result
        """

    def enqueue(self, e):
        self._data.insert(self._data[-1], e) #self._data.append(e)



