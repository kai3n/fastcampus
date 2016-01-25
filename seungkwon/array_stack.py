class Empty(Exception):
    pass

class makeStack():

    def __init__(self):
        self.size =0
        self.newstack =list()

    def __len__(self):
        return len(self.newstack)

    def push(self, data):
        try:
            self.newstack.append(data)
        except:
            raise Empty
        self.size += 1

    def pop(self):
        try:
            mid = self.newstack[self.size-1]
            del self.newstack[self.size-1]
            self.size -= 1
            return mid
        except:
            raise Exception

    def is_empty(self):
        if self.size == 0:
            return False
        else:
            return True

    def top(self):

        if self.size == 0:
            raise Empty

        return self.newstack[self.size-1]

mStack = makeStack()
mStack.push(5)
mStack.push(3)
mStack.push(3)
mStack.push(3)
mStack.pop()
print("ddd----------r",len(mStack))
print("len",mStack.__len__)
print(mStack.is_empty())
print (mStack)



class stack_custom():


    def __len__(self):
        return len(self._data)

    def __init__(self):
        self._data = list()
        self.size = 0

    def push(self, data):
        try:
            self._data.append(data)
        except:
            raise Exception
        self.size += 1

    def is_empty(self):
        if self.size == 0:
            return False
        else:
            return True


    def pop(self):
        mid = self._data[self.size-1]
        try:
            del self._data[self.size-1]
        except:
            raise Exception
        self.size -= 1
        return mid

    def top(self):
        return self._data[self.size-1]

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

for a in third:
    if a == "(" or a == "{" or a == "[":
        mStack.push(a)
    elif mStack.is_empty():
        if mStack.top() == "(" and a == ")":
            mStack.pop()
        elif mStack.top() == "{" and a == "}":
            mStack.pop()
        elif mStack.top() == "[" and a == "]":
            mStack.pop()
    else:
        # 처음 ), }, ] 가 왔을때 바로 입력부터 해준다
        mStack.push(a)
    print(mStack.newstack)

if len(mStack) == 0:
    print(True)
else:
    print(False)
