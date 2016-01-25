class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        a = len(self.data)
        return a

    def push(self, num):
        self.data.append(num)
        return self.data

    def pop(self):
        b = self.data[0]
        self.data.remove(b)
        return b

    def is_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False

    def top(self):
        c = len(self.data)
        return self.data[c-1]

###
