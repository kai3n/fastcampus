
class Empty(Exception):
    pass


class ArrayQueues:

    def __init__(self):
        self.data = []


    def __len__(self):
        return len(self.data)

    def enqueue(self, num):
        return self.data.append(num)

    def dequeue(self):
        how_long=len(self.data)
        if how_long==0:
            return "Error"
        else :
            re_data = self.data[0]
            self.data = self.data[1:len(self.data)]
            return re_data

    def is_empty(self):
        if len(self.data)==0:
         return True
        else :
         return False


    def first(self):
          if len(self.data)==0:
            return False
          else :
              return self.data[0]


Q = ArrayQueues()
Q.enqueue(5)
Q.enqueue(3)
print(len(Q))
print(Q.dequeue())
print(Q.is_empty())
print(Q.dequeue())
print(Q.is_empty())
print(Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print(Q.first())
Q.enqueue(4)
print(len(Q))
print(Q.dequeue())