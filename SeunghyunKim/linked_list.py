class LinkedList:

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

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def add_first(self, e):
        x = self.Node(e, None)
        if self._size == 0:
            self._head = x
            self._tail = x
        else:
            x._next = self._head
            self._head = x
        self._size += 1

    def add_last(self, e):
        x = self.Node(e, None)
        if self._size == 0:
            self._head = x
            self._tail = x
        else:
            self._tail._next = x
            self._tail = x
        self._size += 1

    def remove_first(self):
        if self._size == 0:
            print ("error")
        else:
            self._head = self._head._next
            self._size -= 1

    def remove_last(self):
        if self._size == 0:
            print ("error")
        else:
            n = self._size
            for i in range(1, n-1):
                tail = self._head._next
            self._tail = tail
            self._size -= 1

    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element

    def print_list(self):
        pass

lst = LinkedList()
print(lst.is_empty()) #True
lst.add_first(1)
print(lst.head())   #1
lst.add_first(2)    #2>1
print(lst.head())   #2
print(lst.tail())   #1
lst.add_first(3)    #3>2>1
print(lst.head())   #3
print(lst.tail())   #1
lst.add_last(7)     #3>2>1>7
print(lst.tail())   #7
print(lst.__len__())#4
lst.remove_last()   #3>2>1
print(lst.head())   #3
print(lst.tail())   #1
print(lst.__len__())#3
# lst.add_last(4)
# print(lst.tail())   #4
# lst.add_last(5)     #3->2->1->4->5
# lst.add_last(6)     #3->2->1->4->5->6
# lst.remove_first()  #2->1->4->5->6
# lst.remove_last()   #2->1->4->5
# lst.print_list()    #2->1->4->5
# print(lst.is_empty()) #False
# len(lst)            #return 4