class Empty(Exception):
    pass


class Doublelinkedlist:

    class Node:

        def __init__(self, element, prev, next):
            # element : data /  prev, next : node
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
        if self._size:
            return False
        else:
            return True

    def add_first(self, e):
        if self._size == 0:
            new_node = self.Node(e, None, None)
            self._tail = new_node
        else:
            new_node = self.Node(e, None, self._head)
            self._head._prev = new_node

        self._head = new_node
        self._size += 1

    def add_last(self, e):
        new_node = self.Node(e, None, None)

        if self._size == 0:
            self._head = new_node
        else:
            new_node._prev = self._tail
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1



    # 노드 반환?
    def remove_first(self):
        if self._size == 0:
            raise Empty("error")
        elif self._size == 1:
            self._head, self._tail = None, None
            self._size = 0
        else:
            self._head = self._head._next
            del self._head._prev
            self._head._prev = None
            self._size -= 1


    # 노드 반환?
    def remove_last(self):
        if self._size == 0:
            raise Empty("error")
        elif self._size == 1:
            self._head, self._tail = None, None
            self._size = 0
        else:
            self._tail = self._tail._prev
            del self._tail._next
            self._tail._next = None
            self._size -= 1


    # def insert(self, e):
    #     if self._size == 0:
    #         self.add_first(self, e)
    #     elif self._size == 1:
    #         self.add_last(self,e)



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
