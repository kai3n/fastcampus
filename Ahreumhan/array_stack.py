class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self._data = []
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self._data == []

    def push(self, e):
        self._data.append(e)

    def top(self):
        self._data[len(self._data)-1]


    def pop(self):

        return self._data[len(self._data)-1]