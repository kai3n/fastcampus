class Empty(Exception):
    pass

class LinkedList :

    class _Node:#리스트 내에 선언된 '노드'를 만들어 내는 내부 클래스'
        #이것이 있음으로써 링크스택 클래스 내부에서 특정하게 쓰이는 클래스가 선언된 것이라고 볼 수 있다.

        def __init__(self, element, next=None, prev=None):
            self._element = element#노드는 정보값과
            self._next = next#다음 노드를 가르키는 값을 갖는다.
            self._prev = prev

    def __init__(self):
        self._head=None#링크드리스트 속 클래스 안에는 머릿부분을 가르키는 머릿값이 들어있다.
        self._size =0#이 리스트의 크기가 얼마인지도 알아야하기 때문에
        self._tail =None# 꼬릿값도 필요하다.

    def __len__(self):
        return self._size
    def print_list(self):
        probe = self._head
        while probe is not self._tail:
            print(probe._element,'<->',end=' ')
            probe = probe._next
        print(probe._element)

    def is_empty(self):
        if self._size == 0:
            return True
        else :
            return False



    def add_first(self, element):
        node = self._Node(element)
        #노드에 새로운 값을 넣어주고
        if self._size == 0:#만약에 링크드리스트 안에 아무런 노드도 없을 경우에는
            self._head = node#머릿값에다가 새로 만든 노드를 넣어준다.
            self._tail = node#꼬릿값도 마찬가지다 어짜피 리스트 안에 노드가 한 개밖에 없어서 머리도, 꼬리도 된다.
            self._size+=1
        else:
            self._head._prev = node#머릿값의 이전 값을 노드로 선언
            node._next = self._head#
            self._head = node
            self._size+=1



    def add_last(self, element):
        node = self._Node(element)
        #노드에 새로운 값을 넣어주고
        if self._size == 0:
            self._head = node#머릿값에 새로운 노드를 넣어줌
            self._tail = node#꼬리도 마찬가지
            self._size+=1
        else :
            node._next = None
            node._prev =  self._tail
            self._tail._next = node#꼬리 부분에 있는 노드의 next는 새로 만든 노드!
            self._tail = node#이제 부터 꼬리는 새로만든 노드임
            self._size+=1

    # def add_between(self, element, between_first_num):
    #     node = self._Node(element)
    #     check_serch = self._head
    #
    #     while(check_serch._element != between_first_num):
    #         check_serch = check_serch.next
    #
    #     check_serch = check_serch.next

    def remove_first(self):
        if self._size==0:
            print("error")
        else:
            self._head = self._head._next
            del(self._head._prev)
            self._size-=1

    def remove_last(self):
        if(self._size == 0):
            raise("error")

        elif(self._size == 1):
            self.remove_first()

        else:
            self._tail = self._tail._prev
            del(self._tail._next)
            self._size-=1

    def head(self):
        return self._head._element
    def tail(self):
        return self._tail._element

lst = LinkedList()
print(lst.is_empty()) #True
#print(lst.tail()) #return 1

lst.add_first(1)  #1
print(lst.head()) #return 1
lst.add_first(2)  #2->1
lst.add_first(3)  #3->2->1
lst.print_list()

#print(lst.tail()) #return 1
lst.print_list()
lst.add_last(4)  #3->2->1->4
lst.add_last(5)  #3->2->1->4->5
lst.add_last(6)  #3->2->1->4->5->6
lst.print_list()

lst.remove_first()  #2->1->4->5->6
lst.remove_last()  #2->1->4->5
lst.print_list()

#lst.print_list()  #2->1->4->5
#print(lst.is_empty()) #False
print(len(lst))  #return 4