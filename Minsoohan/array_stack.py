
class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, num):
        self.data.append(num)

    def pop(self):
        how_long = len(self.data)
        if how_long == 0:
            return "Error"
        else :
            re_data = self.data[how_long-1]
            self.data = self.data[:how_long-1]
            return re_data


    def is_empty(self):
        if self.data:
            return False
        else :
            return True

    def top(self):
       if len(self.data)==0:
           return print("Error")
       else:
           return self.data[len(self.data)-1]


S=ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
print(S.pop())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
S.push(8)
print(S.pop())
