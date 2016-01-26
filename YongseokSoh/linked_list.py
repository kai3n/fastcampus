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

    def __str__(self):
        return (str(self._head), str(self._tail), str(self._size))

    def is_empty(self):
        return bool(self._size)

    def add_first(self, node):
        node.next = self._head
        self._head = node
        self._size += 1

    def add_last(self, node):
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
            while probe._next is not self._tail:
                probe = probe._next
            probe._next = None
            self._tail = probe
            self._size -= 1

    def head(self):
        return self._head

    def tail(self):
        return self._tail


l = LinkedList()

l.Node()

