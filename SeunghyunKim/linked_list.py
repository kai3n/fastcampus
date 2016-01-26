class LinkedList:

    class _Node:

        def __init__(self, element):
            self._element = element
            self._next = None

    def __init__(self):

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return len(self)

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def add_first(self, e):

        x = self._Node(e)

        if (self._head == None):
            self._head = e
            self._tail = e
        else:
            x._next = self._head
            self._head = x

        self._size += 1

    def add_last(self, e):

        x = self._Node(e)

        if (self._size == 0) :
            self.add_first(e)
        else:
            self._tail._next = x
            self._tail = x
            self._size += 1


    def remove_first(self):

        if (self._size == 0):
            print("error")
        else:
            self._head = self._head._next
            self._size -= 1

    def remove_last(self):
        pass

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def print_list(self):
        pass

lst = LinkedList()
print(lst.is_empty()) #True
lst.add_first(1)
print(lst.head())   #1
lst.add_first(2)
print(lst.head())   #2
lst.add_first(3)
print(lst.head())   #3
print(lst.tail())   #1
lst.add_last(4)
print(lst.tail())   #4
lst.add_last(5)     #3->2->1->4->5
lst.add_last(6)     #3->2->1->4->5->6
lst.remove_first()  #2->1->4->5->6
lst.remove_last()   #2->1->4->5
lst.print_list()    #2->1->4->5
print(lst.is_empty()) #False
len(lst)            #return 4