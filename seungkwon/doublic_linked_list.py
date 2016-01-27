class EmptyLinked(Exception):
    pass


class DoubleMyLinkedList:
    """
    double
    """
    class Node:
        def __init__(self, element, prev, mNext):
            self._element =element
            self._prev = prev
            self._next = mNext

    def __init__(self):
        self._head = self.Node(None, None, None)
        self._tail = self.Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size


    def is_empty(self):
        return self._head._next is None


    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element

    def add_first(self, element):
        """
        앞으로 저장함
        1. 새로운 데이터의 next는 head(첫번째 데이터)와 동일한것을 본다
        2. head는 mData를 본다
        3. size += 1
        :param element: 데이터
        :return:
        """
        mData = self.Node(element, self._head, None)
        # 가장 마지막 next는 비어있음
        if self.is_empty():
            self._head._next = mData
            mData._next = self._tail
            self._tail._prev = mData
        else :
            self._head._next._prev = mData
            mData._next =self._head._next
            self._head._next = mData

        self._size += 1

    def add_last(self, element):
        """
        tail쪽으로 저장함
        :param element:
        :return:
        """
        mData = self.Node(element, None, self._tail)
        if self.is_empty():
            self._tail._prev = mData
            mData._prev = self._head
            self._head._next = mData
        else :
            self._tail._prev._next = mData
            mData._prev = self._tail._prev
            self._tail._prev = mData
        self._size += 1

    def remove_first(self):
        """
        head가 보고있는것을 삭제함
        1. head의 next값을 저장함
        2. head.next의 값을 삭제
        3. head 는 1의 저장값을 본다
        4. size -= 1
        :return:
        """
        if self.is_empty():
            raise EmptyLinked

        dele = self._head._next
        self._head._next._next._prev = self._head
        self._head._next = self._head._next._next
        del dele
        self._size -= 1

    def remove_last(self):
        """
        tail이 보고 있는것을 삭제
        1. head에서 타고 들어가서 tail -1 을 찾는다
        2. 1의 next를 삭제
        3. tail 이 1을 저장하고
        4. tail.next를 삭제함
        5. size -= 1
        :return:
        """
        if self.is_empty():
            raise EmptyLinked

        dele = self._tail._prev
        self._tail._prev._prev._next = self._tail
        self._tail.prev = self._tail._prev._prev
        del dele
        self._size -= 1

    def print_list(self):
        """
        list내의 모든 내용을 출력함
        :return:
        """
        cur = self._head
        while cur._next:
            print(cur._element)
            cur = cur._next
        print(cur._element, "\nlast")

    def is_empty(self):
        return self._size == 0


    def head(self):
        return self._head._next._element

    def tail(self):
        return self._tail._prev._element

lst = DoubleMyLinkedList()
print(lst.is_empty(), False) #True
lst.add_first(1)  #1
print(lst.is_empty(), True)
print("head", lst.head(), 1) #return 1
lst.add_first(2)  #2->1
lst.add_first(3) #3->2->1
print("---------")
lst.print_list()
print("---------")
#
print("tail",lst.tail(), 1) #return 1
lst.add_last(4)  #3->2->1->4
lst.add_last(5)  #3->2->1->4->5
lst.add_last(6)  #3->2->1->4->5->6
lst.remove_first()  #2->1->4->5->6
lst.remove_last()  #2->1->4->5
print("---------")
lst.print_list() #2->1->4->5
print("---------")
print(lst.is_empty()) #False
print(len(lst))  #return 4