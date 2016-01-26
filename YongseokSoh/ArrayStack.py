class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) is 0:
            return True
        else:
            return False

    def push(self, e):
        return self.data.append(e)

    def top(self):
        if len(self.data) is 0:
            raise Empty("Array is Empty")
        else:
            return self.data[-1]

    def pop(self):
        if len(self.data) is 0:
            raise Empty("Array is Empty")
        elif len(self.data) is 1:
            pop_data = self.data[0]
            self.data = []
            return pop_data
        else:
            pop_data = self.data[len(self.data)-1]
            self.data = self.data[:len(self.data)-1]
            return pop_data


# S = ArrayStack()
#
# S.push(5)
#
# print(S.data)
# S.push(3)
# print(S.data)
# print(len(S))
# print(S.pop())
# print(S.is_empty())
# print(S.pop())
# print(S.data)
# print(S.is_empty())
# S.push(7)
# print(S.data)
# S.push(9)
# print(S.data)
# S.push(4)
# print(S.data)
# print(len(S))
# print(S.pop())
# S.push(6)
# print(S.data)
# S.push(8)
# print(S.data)
# print(S.pop())
# print(S.data)
# print(S.top())