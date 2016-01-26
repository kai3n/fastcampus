
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
     if len(self.data)!=0:
        self.a = self.data[0]
        self.data = self.data[1:len(self.data)]
        return self.a
     else :
        return False

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