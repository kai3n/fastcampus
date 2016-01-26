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
        return len(self)

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def add_first(self, e):

        x = self.Node(e, None)

        if (self._head == None):
            self._head = e
            self._tail = e
        else:
            x._next = self._head
            self._head = x._element

        self._size += 1

    def add_last(self, e):
        Linkedlist.Node(self._head._next, e)
        self._tail = e
        self.size += 1

    def remove_first(self):
        self._head = Linkedlist.Node(self._head._next)
        self.size -= 1

    def remove_last(self):
        pass

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def print_list(self):
        pass

lst = Linkedlist()
print(lst.is_empty())
lst.add_first(1)
print(lst.head())
lst.add_first(2)
print(lst.head())
lst.add_first(3)
print(lst.head())
print(lst.tail())