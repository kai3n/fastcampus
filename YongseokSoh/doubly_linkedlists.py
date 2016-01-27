class DoublyLinkedList:

    class Node:

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._head = self.Node(None, None, None)
        self._tail = self._head
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def print_list(self):
        probe = self._head
        while probe is not self._tail:
            print(probe._element,'->',end=' ')
            probe = probe._next
        print(probe._element)

    def is_empty(self):
        return not bool(self._size)

# Doubly implementation
    def add_first(self, element):
        node = self.Node(element, None, None)
        if self._size is 0:
            self._head = node
            self._tail = node
            self._size = 1
        else:
            node._next = self._head
            self._head._prev = node # doubly implementation
            self._head = node
            self._size += 1

# Doubly implementation
    def add_last(self, element):
        node = self.Node(element, None, None)
        if self._size is 0:
            self._head = node
            self._tail = node
            self._size = 1
        else:
            node._next = None
            node._prev = self._tail # doubly implementation
            self._tail._next = node
            self._tail = node   # self._tail 을 node 로 덮어씀
            self._size += 1

# Doubly implementation
    def remove_first(self):
        if self._size is 0:
            print("List is empty")
        elif self._size is 1:
            self._head = self.Node(None, None, None)
            self._tail = self._head
            self._head._next = self._tail
            self._tail._prev = self._head
            self._size = 0
        else:
            self._head = self._head._next
            del self._head._prev
            self._head._prev = None
            self._size -= 1

# Doubly implementation
    def remove_last(self):
        if self._size is 0:
            print("List is empty")
        elif self._size is 1:
            self._head = self.Node(None, None, None)
            self._tail = self._head
            self._head._next = self._tail
            self._tail._prev = self._head
            self._size = 0
        else:
            self._tail = self._tail._prev
            del self._tail._next
            self._tail._next = None
            self._size -= 1

    def insert_between(self, element, predecessor, successor):
        pass

    def search_node(self, node):
        probe = self._head
        while(probe._element is not node): # searching process
            if probe._next is None: # when searched through whole list
                print("No such node with given value : {}".format(node))
                return None
            else:
                probe = probe._next
        return probe

    def delete_node(self, node):
        del_node = self.search_node(node)
        if del_node:
            del_node._prev._next = del_node._next
            del_node._next._prev = del_node._prev
            del del_node
            self._size -= 1

    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element


lst = DoublyLinkedList()
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
lst.remove_last()  #2->1->4
lst.remove_last()  #2->1
lst.add_last(4)  #2->1->4
lst.add_last(5)  #2->1->4->5
lst.add_last(6)  #2->1->4->5->6

lst.print_list()
lst.remove_last()  #2->1->4->5
lst.print_list()
lst.remove_last()  #2->1->4
lst.print_list()
lst.remove_last()  #2->1
lst.print_list()
lst.remove_last()  #2
lst.print_list()
lst.remove_last()  #0
lst.print_list()
print(lst.is_empty()) #True
lst.add_first(22)
lst.print_list()
lst.remove_first()
lst.remove_first()
lst.remove_first()
lst.add_first(12)
lst.add_first(13)
lst.add_first(14)
lst.add_last(15)
lst.print_list()
lst.delete_node(12)
lst.delete_node(13)
lst.delete_node(20)

lst.print_list()

print(lst.is_empty()) #True

#lst.print_list()  #2->1->4->5
#print(lst.is_empty()) #False
#print(len(lst))  #return 4

