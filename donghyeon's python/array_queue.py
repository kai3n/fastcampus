class Empty(Exception):
    pass
class ArrayQueue:

    def __init__(self):

        self._data= []
        self._size = 0
        self._front = 0
    def __len__(self):                            #AQ_size 가 0이다 왜냐하면 위에 self._data = 빈 리스트기때문에
        return self._size
    def is_empty(self):                            # 지금 빈리스트라 트루를 반환함
        if self._size ==0:
            return True

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        eng = self._data[0]            #eng 를 가장 먼처들어간 데이터라고보고
        del self._data[0]                  # 가장먼저들어온 데이터 삭제   (큐의 특징)
        return eng                      #삭제된후 리스트 반환
    def first(self):
        if len(self._data) == 0:            #데이터의 길이가 0일때 즉 빈리스트일때 에러값을 띄움
            raise Empty("큐는 없다 ")
        else:
            return self._data[0]            # 빈리스트가 아니면 처음들어간 데이터를 반환한다.


AQ = ArrayQueue()
print(len(AQ))
print(AQ.is_empty())
print(AQ._data.append(2))
print(AQ._data)
print(AQ._data.append(3))
print(AQ._data.append(4))
print(AQ._data)
print(AQ.dequeue())
print(AQ._data)
print(AQ.first())







