class Empty(Exception):
    raise Exception

class stack_custom():

    def __len__(self):
        return self.__len__

    def __init__(self):
        self._data = list()

    def push(self, data):
        try:
            print(data)
            self._data.append(data)

        except:
            raise Exception
        self.__len__ += 1

    def is_empty(self):
        if self.__len__() == 0:
            return False
        else:
            return True


    def pop(self):
        mid = self._data[self.__len__()]
        try:
            del self._data[self.__len__()-1]
        except:
            raise Exception
        self.__len__ -= 1
        return mid

    def top(self):
        return self._data[self.__len__()-1]

mStack = stack_custom()
mStack.push(5)
mStack.push(3)
print (mStack._data)