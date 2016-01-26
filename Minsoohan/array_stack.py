
class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, num):
        self.data.append(num)
        return self.data

    def pop(self):
        if len(self.data)==0:
            raise Empty('No Value')
        else :
            pop_data = self.data[:len(self.data)-1]
            return pop_data

    def is_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False

    def top(self):
        b = len(self.data)
        return self.data[b-1]

