class Linkedlist :

    class _Node:

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head=None
        self._size =0
        self._tail =None


    def __len__(self):
        return self._size

    def is_empty(self):
        if self._head==None:
            return True
        else :
            return False

    def add_first(self, element):
        n1 = self._Node(element)#add를 해줄 때마다 노드를 새로 만들어야 하기 때문에
        #add_first함수에 노드 인스턴스를 만들어준다.
        if self._head==None:#만약에 클래스 안의 헤드값에 아무것도 없을 경우
            self._head=n1#지금 만든 노드를 헤드로 만들어버린다.
            self._tail=n1#혹시나 tail부분에 데이터를 붙여야 할 수도 있으니까 tail로도 설정해준다.
            self._size+=1

        else :#만약에 헤드가 이미 있을 경우에는 이미 있는 노드의 헤드를 지금만든 걸로 뺏어와야한다.
            n1._next=self._head#현재 있는 헤드를 n1노드의 다음부분으로 만들어버린다.
            self._head = n1#헤드를 새로 선언해준다.
            self._size+=1#전체 사이즈를 1 늘린다.

    def add_last(self, element):
        n1=self._Node(element)#새로운 노드 설정
        if self._head==None:#만약에 클래스 안에 헤드값에 아무것도 없을경우
            self._head=n1
            self._tail=n1
            self._size+=1
        else :#뭔가 있을 경우
            n1._next=None
            self._tail.next=n1
            self._tail=n1
            self._size+=1

    def remove_first(self):
        if self._head==None:
            return print("리스트에 아무것도 존재 하지 않습니다.")

        else :
            self._head = self._head._next
            self._size-=1

    def remove_last(self):

        if self._head==None:
            return print("리스트에 아무것도 존재하지 않습니다.")
        else:
            self._tail = self._tail._next
            self._size-=1


L=Linkedlist()

print(L.is_empty())

L.remove_first()


