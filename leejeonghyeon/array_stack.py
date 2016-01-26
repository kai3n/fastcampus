class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data) <= 0:
            return True
        else:
            return False

    def push(self, e):
        self._data.insert((len(self._data)+1), e)
        return self._data

    def top(self):
        if len(self._data) <= 0:
            raise Empty("error")
        else:
            return self._data[-1]

    def pop(self):
        if len(self._data) <= 0:
            raise Empty("error")
        else:
            pop_e = self._data[-1]
            del self._data[-1]
        return pop_e