class Empty(Exception):
    pass


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

mQueue = array_queue()
print(mQueue.is_empty())
mQueue.enqueue(1)
mQueue.enqueue(2)
mQueue.enqueue(3)
mQueue.enqueue(4)
mQueue.enqueue(5)
print(mQueue.data)
mQueue.dequeue()
mQueue.dequeue()
print(mQueue.data)
print(mQueue.is_empty())
print(len(mQueue))
mQueue.dequeue()
print(mQueue.first())