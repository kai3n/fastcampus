class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self._data = []
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        a = len(self._data)
        if a == 0:
          return True

        else:
          return False

    def push(self, e):
        self._data.append(e)

    def top(self):
        self._data[len(self._data)-1]

    def pop(self):

        return self._data[len(self._data)-1]