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

    def is_empty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def add_first(self, el):
        new1 = self.Node(el, next)

        if self._size == 0:
            new1._next = None
            self._head = new1
            self._tail = new1
            # self._temp = new1
            self._size += 1
        else:
            new1._next = self._head
            self._head = new1
            self._size += 1

    def add_last(self, el):
        new1 = self.Node(el, None)

        if self._size == 0:
            self._head = new1
            self._tail = new1
            self._size += 1
        else:
            self._tail._next = new1
            self._tail = new1
            self._size += 1

    def remove_first(self):
        if self._size == 0:
            print('the list is empty')
        else:
            a = self._head
            self._head = self._head._next
            a._next = None
            self._size -= 1

    def remove_last(self):
        if self._size == 0:
            print('the list is empty')
        else:
            a = self._head
            while a._next != self._tail:
                a = a._next
            self._tail = a
            a._next = None
            self._size -= 1

    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element

    def print_list(self):
        if self._size == 0:
            print('the list is empty')
        else:
            a = self._head
            while a != self._tail:
                print(a._element, '->', end=' ' )
                a = a._next
            print(a._element)


lst = LinkedStack()
# print(lst.is_empty()) #True
lst.add_first(1)
#1
# print(lst.head()) #return 1
lst.add_first(2)  #2->1
lst.add_first(3)  #3->2->1
# print(lst.tail()) #return 1
# print(lst.head())
lst.add_last(4)  #3->2->1->4
# print(lst.tail()) #4
lst.add_last(5)  #3->2->1->4->5
lst.add_last(6)  #3->2->1->4->5->6
lst.print_list()
# print(lst.tail()) #6
lst.remove_first()  #2->1->4->5->6
# print(lst.tail())
lst.remove_last()  #2->1->4->5
# print(lst.tail())
lst.print_list()  #2->1->4->5
print(lst.is_empty()) #False
print(len(lst))  #return 4
