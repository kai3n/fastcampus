class Linkedlist:
    class Node:
            def __init__(self, element, next):
                self._element = element
                self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size           #빈 노드의 사이즈를 반환함


    def is_empty(self):
        if self._head == None:              #헤드가 0 이다 즉 노드가 없다일떄 Ture 반환
            return True
        else:
            return False

    def add_first(self, e):
        new = self.Node(e, None)       #새로운 노드생성 그노드의 성분과 가르키는 값으로 2파라마타가옴
        if self._size==0:      #즉 노드가 아무것도 없을
            self._head = new    #새로운 노드를 헤드로 정함 왜? 기존에 아무것도 없었으니까
            self._tail = new    #새로운 노드를 꼬리로 정함 왜? 기존에 아무것도없었으니까
            self._size = self._size +1 # 새로운노드가 하나생겼으니 데이터사이즈를 늘려줌
        else:                                   #하지만 기존의 노드가 있을때
            new._next = self._head              #새로만든 노드의 포인터(연결방향)을 기존의 헤드로 향함
            self.head = new                     #그리고 새로만든 노드를 헤드로 정해줌
            self._size = self._size +1          #똑같이 사이즈업

    def add_last(self, e):
        new = self.Node(e, None)        #새로운노드를 정의함
        if self._size ==0:              #빈노드일때
            self._head = new            # 새로운 노드를 헤드로만들고    \
            self._tail = new            # 새로운 노드를 꼬리로 만들고
            self._size = self._size + 1 # 사이즈업
        else:                                   #만약 빈노드가아니면
            new.next = None                     #우선 새로운노드의 포인터를 none으로 가리킴 (마지막에 붙이기때문)
            self._tail._next = new              #그리고 기존에 있던 꼬리의 포인터를 새로운 노드로가리킴
            self._tail = new                    #그리고 새로운 노드를 꼬리로 가르킴
            self._size = self._size +1          #그리고 사이즈업

    def remove_first(self):
        if self._size == 0:                 # 빈노드일떄 지울수없으니 애러를 발생시켜줌
            raise Exception ("Error There is no Node")
        else:                                   # 노드가 존재할때
            self._head = self._head._next        # 헤더의 포인터가 가르키는 노드를 헤드로 지정
            self._size = self._size -1          # 노드 하나빼줌

    def remove_last(self):
        if self._size ==0:
            raise Exception("Error There is no Node")
        else:
            current = self._head
            a= object
            while current._next:
                a =current
                current = current._next
            a._next = None
            self._tail = a
            self._size -= 1


        # else 일때 데이터가 앞에서 부터 찾으니까
        # 앞에서 부터 데이터값을 뽑은다음 마지막을
        # 제거해주는식으로해야하나..?

    def head(self):                 # 헤더는 요소의 헤더를 리턴해줌
        return self._head._element  # 그냥 head 를 정의해줘야한다하나 이게없으면 헤드 값이 프린트안됨


    def tail(self):                  # 꼬리  정의해줌
        return self._tail._element

    def print_list(self):
        cur = self._head
        while cur._next:  #여기에선 트룬지 폴슨지만 확인   #와일이 트루일때까지 계속 루프돔
            print(cur._element)
            cur = cur._next      #기존에 커텐ㅌ 는 커렌트가 가르키는 값이다. 즉 다음꺼 계속 보여달란거
        print(cur._element)
       # self._head._next._next._next._next._element
#
#
# lst = Linkedlist()
# print(lst.is_empty(), True) #True
# lst.add_first(1)  #1
# print(lst.head(), 1) #return 1
# lst.add_first(2)  #2->1
# lst.add_first(3) #3->2->1
# lst.print_list()
# print(lst.tail(), 1) #return 1
# lst.add_last(4)  #3->2->1->4
# lst.add_last(5)  #3->2->1->4->5
# lst.add_last(6)  #3->2->1->4->5->6
# lst.remove_first()  #2->1->4->5->6
# lst.remove_last()  #2->1->4->5
# lst.print_list()  #2->1->4->5
# print(lst.is_empty()) #False
# print(len(lst))  #return 4












# lst = Linkedlist()
# print(lst.is_empty()) #True
# print("----------------")
#
# lst.add_first(1)  #1
# print("h",lst.head()) #return 1
# lst.add_first(2)  #2->1
# lst.add_first(3) #3->2->1
#                              #현재 노드 1 2 3을 차례대로 헤드자리에 넣어서 3->2->1 이됬는데 어떻게 프린트를찍어서 연결된 노드를 볼수있을까?
# print(lst.tail()) #return 1
# lst.add_last(4)  #3->2->1->4
# lst.add_last(5)  #3->2->1->4->5
# lst.add_last(6)  #3->2->1->4->5->6
# lst.remove_first()  #2->1->4->5->6
# lst.remove_last()  #2->1->4->5
# lst.print_list()  #2->1->4->5
# print(lst.is_empty()) #False
# len(lst)  #return 4

















# LD = Linkedlist()
#
# print(LD._size)
# print(LD.is_empty())
# LD.add_first(1)
# print(LD._size)
# LD.add_first(2)
# print(LD._size)
# LD.add_first(3)
# print(LD._size)
#
# LD.add_last(4)
# # LD.add_last(5)
# #LD.add_last(6)
#
#
# class Empty(Exception):
#     pass
# class Linkedlist:
#     class Node:
#         def __init__(self, element, next):
#             self._element = element
#             self._next = next
#         def __init__(self):
#             self._head= None
#             self._tail= None
#             self._size= 0
#
#
#         def __len__(self):
#             return self._size
#
#
#
LL = Linkedlist()
print(LL.is_empty(),True) #True
LL.add_first(1)  #1
print(LL.head()) #return 1
LL.add_first(2)  #2->1
LL.add_first(3)  #3->2->1
print(LL.tail())#return 1
print("-------")
print()

LL.add_last(4)  #3->2->1->4
LL.add_last(5)  #3->2->1->4->5
LL.add_last(6)  #3->2->1->4->5->6
LL.remove_first()  #2->1->4->5->6
LL.remove_last()  #2->1->4->5
LL.print_list()  #2->1->4->5
print(LL.is_empty()) #False
len(LL)  #return 4

#
