class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        print("start")
        self._data = []
        print("end")

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data) <= 0:
            return True
        else:
            return False

    def push(self, e):
        stack_len = len(self._data)
        self._data.insert((stack_len+1), e)
        return self._data

    def top(self):
        return self._data[len(self._data)-1]

    def pop(self):
        if len(self._data) <= 0:
            raise Empty("error")
        else:
            pop_e = self._data[len(self._data)-1]
            del self._data[len(self._data)-1]
        return pop_e
