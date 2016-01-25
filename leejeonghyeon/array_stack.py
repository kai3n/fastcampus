class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        pass

    def is_empty(self):
        if len(self._data) ==0:
            return True

    def push(self, e):
        stack_len =len(self._data)
        self._data.insert((stack_len+1),e)
        return self._data

    def top(self):
        return self._data[len(self._data)-1]

    def pop(self):
        pop_e = self._data[len(self._data)-1]
        del self._data[len(self._data)-1]
        return pop_e
