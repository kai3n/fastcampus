class ArrayQueue:
    def __init__(self):
        self._data = []

    def __len__(self):
        print ("length is",len(self._data))

    def is_empty(self):
        if(len(self._data) == 0):
            print("it`s empty")
        else:
            print("is not empty")

    def enqueue(self, e):
        self._data.append(e)

    def first(self):
        print(self._data[0])

    def dequeue(self):
        if(len(self._data) == 0):
            print ("error")
        else:
            print(self._data[0])
            del (self._data[0])

Q = ArrayQueue()

Q.enqueue(5)
Q.enqueue(3)
Q.__len__()
Q.dequeue()
Q.is_empty()
Q.dequeue()
Q.is_empty()
Q.dequeue()
Q.enqueue(7)
Q.enqueue(9)
Q.first()
Q.enqueue(4)
Q.__len__()
Q.dequeue()