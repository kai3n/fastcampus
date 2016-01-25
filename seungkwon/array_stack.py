class Empty(Exception):
    pass

class stack_custom():


    def __len__(self):
        return len(self._data)

    def __init__(self):
        self._data = list()
        self.__len__ = 0

    def push(self, data):
        try:
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

# mStack = stack_custom()
# mStack.push(5)
# mStack.push(3)
# mStack.push(3)
# mStack.push(3)
# mStack.pop()
# print("ddd----------r",len(mStack))
# print("len",mStack.__len__)
# print(mStack.is_empty())
# print (mStack._data)
# print(len(mStack._data))

fir = "()(()){([])}"
sec = "((()(()){([)])}))"
third = ")(()){([])}"

mStack = stack_custom()
for a in sec:
    if a == "(" or a == "{" or a == "[":
        mStack.push(a)
    elif mStack.is_empty():
        if mStack.top() == "(" and a == ")":
            mStack.pop()
        elif mStack.top() == "{" and a == "}":
            mStack.pop()
        elif mStack.top() == "[" and a == "]":
            mStack.pop()
    print(mStack._data)

if len(mStack) == 0:
    print(True)
else:
    print(False)