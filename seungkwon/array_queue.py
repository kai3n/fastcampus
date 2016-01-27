class Empty(Exception):
    pass

class advanced_queue():

    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        try:
            mid = self.queue[self.__len__() -1]
            del self.queue[self.__len__() -1]
            return mid
        except:
            raise Empty

    def first(self):
        if self.__len__ == 0:
            raise Empty
        else:
            return self.queue[self.__len__()-1]

    def is_empty(self):
        """
        비어있으면 true를 반환한다
        :return:
        """
        return len(self.queue) is 0
        # if len(self.queue) == 0:
        #     return True
        # else:
        #     return False

class array_queue():
    def __init__(self):
        self.size = 0
        self.data = list()

    def __len__(self):
        return self.size

    def enqueue(self, e):
        self.data.append(e)
        self.size += 1

    def dequeue(self):
        try:
            res = self.data[0]
            del self.data[0]
            self.size -= 1
            return res
        except:
            raise Empty

    def first(self):
        if self.size == 0:
            raise Empty
        else:
            return self.data[0]

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

mQueue = advanced_queue()
print(mQueue.is_empty())
mQueue.enqueue(1)
mQueue.enqueue(2)
mQueue.enqueue(3)
mQueue.enqueue(4)
mQueue.enqueue(5)
print(mQueue.queue)
mQueue.dequeue()
mQueue.dequeue()
print(mQueue.queue)
print(mQueue.is_empty())
print(len(mQueue))
mQueue.dequeue()
print(mQueue.first())