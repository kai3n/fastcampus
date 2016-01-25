class Empty(Exception):
    pass

class stack_custom():


    def __len__(self):
        return int(self.__len__)

    def __init__(self):

        self._data = list()
        self.__len__ = 0

    def push(self, data):
        try:
            print(data)
            self._data.append(data)
        except:
            raise Exception
        self.__len__ += 1

    def is_empty(self):
        if self.__len__ == 0:
            return False
        else:
            return True


    def pop(self):
        mid = self._data[self.__len__-1]
        try:
            del self._data[self.__len__-1]
        except:
            raise Exception
        self.__len__ -= 1
        return mid

    def top(self):
        return self._data[self.__len__-1]

mStack = stack_custom()
mStack.push(5)
mStack.push(3)
mStack.pop()
print(mStack.is_empty())
print (mStack._data)