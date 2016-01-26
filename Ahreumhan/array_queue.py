
class Empty(Exception):
    pass

class ArrayQueue:

    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):

        return len(self._data)

    def is_empty(self):

        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

    def dequeue(self):

      if self._data[0]:

        return self._data

    def first(self):

      if self._size == 0:

         raise Exception

      else:

        return self._data[0]

