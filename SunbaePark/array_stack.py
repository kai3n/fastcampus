class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self)

    def is_empty(self):
        if len(self) == 0:
            return False
        else :
            return True

    def push(self, e):
        self.data.append(e)


    def top(self):
        return self.data[len(self.data)-1]

    def pop(self):
        a = self.data[len(self.data)-1]
        del(self.data[len(self.data)-1])
        return a