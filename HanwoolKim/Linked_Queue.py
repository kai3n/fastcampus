class Empty(Exception):
    pass


class Linked_Queue:

    class _Node:
        def __init__(self, element):
            self._element = element
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
        else:
            return False

    def add_first(self, e):

        if (self._head == None):
            self._head = e
            self._tail = e
        else:
            e._next = self._head
            self._head = e

        self._size+=1

    def enqueue(self, num):

        e = self._Node(num)
        if(self._size == 0):
            self.add_first(e)

        else:
            self._tail._next = e
            self._tail = e
            self._size+= 1

    def dequeue(self):
        if(self._size == 0):
            raise("error")

        else:
            temp = self._head
            self._head = temp._next
            temp._next = None
            self._size-= 1

    def remove_last(self):
        if(self._size == 0):
            raise("error")

        elif(self._size == 1):
            self.remove_first()

        else:
            temp = self._head

            while(temp._next != self._tail):
                temp = temp._next


            self._tail = temp
            self._tail._next = None


    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def print_list(self):

        temp = self._head
        if temp == None:
            print("empty")

        while(temp != None):
            if(temp._next == None):
                print(temp._element)
                break
            print(temp._element, "-> ", end = " ")
            temp = temp._next


q = Linked_Queue()
q.enqueue(10)
q.enqueue(15)
q.print_list()
q.dequeue()
q.print_list()

