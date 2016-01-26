class Empty(Exception):
    pass

class custom_stack():
    def __init__(self):
        self.data = list() # data
        self.size = 0 # list size

    def __len__(self):
        return self.size #list size

    def push(self, to):
        self.data.append(to)
        # self.size += 1
        self.size = len(self.data)

    def pop(self):
        # 1빠져
        # 보여줘
        # 사이즈 - 1
        res = self.data[self.size-1] #4
        del self.data[self.size-1]
        # print("find:",res)
        self.size -= 1
        return res # 4

    def is_empty(self):
        # empty -> True
        # have datas -> False
        print("test", self.data)
        if self.size == 0:
            return True
        else:
            return False

    def top(self):
        # 제일 위에거
        try:
            return self.data[self.size-1]
        except:
            raise Empty




mystack = custom_stack()


print(len(mystack))
# mystack.push(1)
# mystack.push(2)
# print(mystack.top())
# mystack.push(3)
# mystack.push(4)
# print(mystack.top())
