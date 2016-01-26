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

    def print_list(self):
        probe = self._head
        while probe is not self._tail:
            print(probe._element,'->',end=' ')
            probe = probe.next
        print(probe._element)


    def is_empty(self):
        return not bool(self._size)

    def add_first(self, element):
        node = LinkedList.Node(element, None)
        if self._size is 0:
            self._head = node
            self._tail = node
            self._size = 1
        else:
            node.next = self._head
            self._head = node
            self._size += 1

    def add_last(self, element):
        node = LinkedList.Node(element, None)
        if self._size is 0:
            self._head = node
            self._tail = node
            self._size = 1
        else:
            node.next = None
            self._tail.next = node
            self._tail = node
            self._size += 1

    def remove_first(self):
        if self._head is None:
            print("List is empty")
        else:
            self._head = self._head.next
            self._size -= 1

    def remove_last(self):
        if self._head is None:
            print("List is empty")
        else:
            probe = self._head
            while probe.next is not self._tail:
                probe = probe.next
            probe.next = None
            self._tail = probe
            self._size -= 1

    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element


lst = LinkedList()
print(lst.is_empty()) #True
lst.add_first(1)  #1
print(lst.head()) #return 1
lst.add_first(2)  #2->1
lst.add_first(3)  #3->2->1
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