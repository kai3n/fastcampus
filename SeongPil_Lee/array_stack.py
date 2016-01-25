class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def push(self, e):
        self.data.append(e)
    def top(self):
        return self.data[-1]
    def pop(self):
        if len(self.data) == 0:
            print('error')
        else:
            a = self.data[-1]
            self.data.pop()
            return a


