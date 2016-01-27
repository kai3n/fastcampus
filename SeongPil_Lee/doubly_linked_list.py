class LinkedList:
    class Node:
        def __init__(self, element,prev=None, next= None):
            self._element = element
            self._prev = prev
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
        new1 = self.Node(el)

        if self._size == 0:
            new1._next = None
            new1._prev = None
            self._head = new1
            self._tail = new1
            self._size += 1
        else:
            new1._next = self._head
            self._head._prev = new1
            new1._prev = None
            self._head = new1
            self._size += 1

    def add_last(self, el):
        new1 = self.Node(el)

        if self._size == 0:
            new1._next = None
            new1._prev = None
            self._head = new1
            self._tail = new1
            self._size += 1
        else:
            self._tail._next = new1
            new1._prev = self._tail
            self._tail = new1
            self._size += 1

    def remove_first(self):
        if self._size == 0:
            print('the list is empty')
        else:
            self._head = self._head._next
            self._head._prev = None
            self._size -= 1

    def remove_last(self):
        if self._size == 0:
            print('the list is empty')
        else:
            self._tail = self._tail._prev
            self._tail._next = None
            self._size -= 1

    def insert(self, now_el, e): #현재 엘리먼트(now_el) 뒤에 e를 넣는다
        new1 = self.Node(e)

        if self._size == 0:
            self.add_first(e)
        elif self._size == 1:
            self.add_last(e)
        else:
            now = self._head
            while now._element != now_el:
                now = now._next
            new1._prev = now
            new1._next = now._next
            now._next = new1
            now._next._next._prev = new1

    def remove(self, el):
        if self._size == 0:
            print('empty list')
        elif self._size == 1 and self._head._element == el:
            self._head = None
            self._tail = None
        elif self._size >= 2:
            if self._head._element == el:
                self.remove_first()
            elif self._tail._element == el:
                self.remove_last()
            else:
                pass
            now = self._head
            while now._element != el:
                now = now._next
            front = now._prev
            back = now._next
            front._next = back
            back._prev._next = None
            back._prev._prev = None
            back._prev = front



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


lst = LinkedList()
print(lst.is_empty()) #True
lst.add_first(1)  #1
print(lst.tail()) #return 1

print(lst.head()) #return 1
lst.add_first(2)  #2->1
lst.add_first(3)  #3->2->1
lst.print_list()  #2->1->4->5

print(lst.tail()) #return 1
lst.add_last(4)  #3->2->1->4
lst.add_last(5)  #3->2->1->4->5
lst.print_list()  #2->1->4->5

lst.add_last(6)  #3->2->1->4->5->6
lst.remove_first()  #2->1->4->5->6
lst.remove_last()  #2->1->4->5
lst.print_list()  #2->1->4->5
print(lst.is_empty()) #False
len(lst)  #return 4
print('===================')
lst.remove(1) #2->4->5
lst.print_list()
lst.insert(2,8) #2->8->4->5
lst.print_list()
lst.remove_first() #8->4->5
lst.print_list()