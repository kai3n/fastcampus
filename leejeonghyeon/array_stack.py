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

    def push(self, e):                              # S라는 스택객체의 가장 위에 e라는 엘리먼트를 더한다
        self._data.insert((len(self._data)+1), e)
        return self._data

    def top(self):                                  # S라는 스택객체의 가장 위의 엘리먼트를 삭제하고 반환
        if self.is_empty():
            raise Empty("error")
        else:
            return self._data[-1]

    def pop(self):                                  # S라는 스택객체의 가장 위의 엘리먼트를 삭제하고 반환
        if self.is_empty():
            raise Empty("error")
        else:
            pop_e = self._data[-1]
            del self._data[-1]
        return pop_e