class EmptyLinked(Exception):
    pass

class LinkedStack:
    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def add_first(self, element):
        """
        top -> tail
        가장 처음에 데이터를 추가한다
        :param element: 추가할 데이터
        :return:
        """
        mData = self.Node(element,None)

        # print("inner",self._head._element)
        if self._head == None:
            self._head = mData
            self._tail = mData
        else:
            mData._next = self._head
            self._head = mData
        self._size += 1

    def add_last(self, element):
        """
        가장 나중에 데이터를 추가한다
        :param element: 추가할 데이터
        :return:
        """
        mData = self.Node(element, None)
        if self.is_empty() :
            self._head = mData
            self._tail = mData
        else:
            cur = self._head
            while cur._next:
                cur = cur._next

            cur._next = mData

            # self._tail._next = mData
            self._tail = mData
            self._size += 1
        # self.tail -> None tail.next는 무조건 none이다


    def remove_first(self):
        """
        가장 첫번째 데이터를 삭제함
        :return:
        """
        if self.is_empty():
            raise EmptyLinked
            # list각 비어있는 경우
        else:
            mid = self._head._next # 두번째 데이터
            print("in remoce first",mid._element, mid._next)
            self._head._next = None #첫번째 데이터의 연결선을 끊는다
            self._head = mid #나의 head에 2번째 데이터를 넣는다
            self._size -= 1

    def remove_last(self):
        """
        가장 마지막 데이터를 삭제함
        :return:
        """
        current = self._head
        a = object
        while current._next:
            a = current
            current = current._next
        a._next = None
        self._tail = a
        self._size -= 1


    def print_list(self):
        """
        출력만 담당함
        :return:
        """
        cur = self._head
        while cur._next:
            print(cur._element)
            cur = cur._next
        print(cur._element)

    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element

    def is_empty(self):
        return self._head is None

lst = LinkedStack()
print(lst.is_empty(), True) #True
lst.add_first(1)  #1
print(lst.head(), 1) #return 1
lst.add_first(2)  #2->1
lst.add_first(3) #3->2->1
print("---------")
lst.print_list()
print("---------")

print("ttt",lst.tail(), 1) #return 1
lst.add_last(4)  #3->2->1->4
lst.add_last(5)  #3->2->1->4->5
lst.add_last(6)  #3->2->1->4->5->6
lst.remove_first()  #2->1->4->5->6
lst.remove_last()  #2->1->4->5
lst.print_list()  #2->1->4->5
print(lst.is_empty()) #False
print(len(lst))  #return 4