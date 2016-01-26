class Empty(Exception):
    pass


class Linkedlist:

    class Node:

        def __init__(self, element, next):
            # element : data, next : node
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        if self._size:
            return False
        else:
            return True

    def add_first(self, e):
        if self._size == 0:
            new_node = self.Node(e, None)
            self._tail = new_node
        else:
            new_node = self.Node(e, self._head)

        self._head = new_node
        self._size += 1

    def add_last(self, e):
        new_node = self.Node(e, None)

        if self._size == 0:
            self._head = new_node
        else:
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1


    # 노드 반환?
    def remove_first(self):
        if self._size == 0:
            raise Empty("error")
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
        else:
            self._head = self._head._next
            self._size -= 1


    # 노드 반환?
    def remove_last(self):
        if self._size == 0:
            raise Empty("error")
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
        else:
            node_f = None
            node_b = self._head

            while True:
                if node_b._next:
                    node_f = node_b
                    node_b = node_b._next
                else:
                    break
            node_f._next = None
            self._tail = node_f
            self._size -= 1


    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element

    def print_list(self):
        if self._size == 0:
            print("None")
            return

        node = self._head
        element_list = list()
        while node._next:
            element_list.append(node._element)
            node = node._next
        else:
            element_list.append(self._tail._element)

        print(element_list)

