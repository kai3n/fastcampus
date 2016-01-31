class EmptyLinked(Exception):
    pass


class MyLinkedList:
    """
    배운거 바로 복습
    시작시간 19:30~20:00
    """
    class Node:
        def __init__(self, element, next):
            self._element =element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size


    def add_first(self, element):
        """
        앞으로 저장함
        1. 새로운 데이터의 next는 head(첫번째 데이터)와 동일한것을 본다
        2. head는 mData를 본다
        3. size += 1
        :param element: 데이터
        :return:
        """
        mData = self.Node(element, None)
        # 가장 마지막 next는 비어있음
        if self.is_empty():
            self._tail = mData
            self._head = mData
        else :
            mData._next = self._head
            self._head = mData
        self._size += 1

    def add_last(self, element):
        """
        tail쪽으로 저장함
        :param element:
        :return:
        """
        mData = self.Node(element, None)
        if self.is_empty():
            self._tail = mData
            self._head = mData
        else :
            self._tail._next = mData
            self._tail = mData
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

        mid = self._head._next
        self._head._next = None
        self._head = mid
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

        cur = self._head
        before_tail = None
        while cur._next:
            before_tail = cur
            cur = cur._next
        before_tail._next = None
        self._tail = before_tail
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
        return self._head is None


    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element



lst = MyLinkedList()
print(lst.is_empty(), True) #True
lst.add_first(1)  #1
print("head", lst.head(), 1) #return 1
lst.add_first(2)  #2->1
lst.add_first(3) #3->2->1
print("---------")
lst.print_list()
print("---------")

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










class LinkedStack:
    """
    수업시간중 구현
    """
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
        while cur._next:  #여기에선 트룬지 폴슨지만 확인   #와일이 트루일때까지 계속 루프돔
            print(cur._element)
            cur = cur._next      #기존에 커텐ㅌ 는 커렌트가 가르키는 값이다. 즉 다음꺼 계속 보여달란거
        print(cur._element)
        self._head._next._next._next._next._element

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