class Empty(Exception):
    pass

class LinkedStack():

    class Node():
        def __init__(self, data):
            self._data = data
            self._next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        return False

    def add_first(self, data):
        if self.is_empty:
            self._head = self.Node(data)

        new = self.Node(data)
        new.next = self._head
        head = new
        self._size += 1
        return

    def add_last(self,data):
        new = self.Node(data)
        self._tail.next = new
        tail = new
        self._size += 1
        return

    def remove_first(self):
        if not self._head:
            raise Empty("Empty List")
        self._head = self._head._next
        self._size -= 1
        return

    def remove_last(self):
        # curNode = self._head
        # print(curNode._next)

        if self._size == 0:
            return 'Empty List'

        if self._size == 1:
            del(self._head)
            return

        while self._next._next._next == None:
            cur_node = cur_node._next
            print(cur_node)
        # except:
        #     cur_node = self._head._next

        del(cur_node._next)
        cur_node._next = None
        self._size -= 1
        return

    def head(self):
        print(self._head)

    def tail(self):
        curNode= self._head
        while not self.Node._next._next:
            curNode = curNode._next

        print (curNode._next)

    def print_list(self):
        if self._size == 0:
            print("Empty List")
        if self._size == 1:
            print("self._head")
            print("self._head._next")
        while self._head._next._next:

            head = head._next
            print(head)

a = LinkedStack()

a.add_first(5)
a.add_first(6)
print(a._size)
a.print_list()
a.remove_last()
a.is_empty()
# a.print_list()
