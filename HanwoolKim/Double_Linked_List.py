class Empty(Exception):
    pass

class Doubly_Linked_List:

    class _node:
        def __init__(self, element):
            self._element = element
            self._prev = None
            self._next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        if(self._length == 0):
            return True
        return False

    def add_First(self, e):
        temp = self._node(e)

        if(self._head == None):
            self._head = temp
            self._tail = temp

        else:
            self._head._prev = temp
            temp._next = self._head
            self._head = temp
        self._length += 1

    def add_Last(self, e):
        temp = self._node(e)

        if(self._head == None):
            self.add_First(e)

        else:
            self._tail._next = temp
            temp._prev = self._tail
            self._tail = temp
            self._length += 1

    def remove_First(self):
        if(self._head == None):
            raise ("error")

        else:
            temp = self._head._next
            self._head.next = None
            temp._prev = None
            self._head = temp

        self._length -= 1

    def remove_Last(self):

        if(self._length == 0):
            raise("there is no list")

        elif(self._length == 1):
            self._head = None

        else:
            temp = self._tail._prev
            self._tail._prev = None
            temp._next = None
            self._tail = temp
            self._length -= 1


    def print_List(self):
        temp = self._head

        if(temp == None):
            print("there is no List")

        while(temp != None):
            if(temp._next == None):
                print(temp._element)
            else:
                print(temp._element, "-->", end=" ")

            temp = temp._next




dll = Doubly_Linked_List()
dll.add_First(10)
dll.print_List()
dll.add_First(15)
dll.print_List()
dll.add_Last(20)
dll.print_List()
dll.add_Last(30)
dll.print_List()
dll.remove_First()
dll.print_List()
dll.remove_First()
dll.print_List()
dll.remove_Last()
dll.print_List()
dll.remove_Last()
dll.print_List()


