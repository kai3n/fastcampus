import copy
# hard카피를 위한 패키지

class EmptyLinked(Exception):
    pass


class LinkedQueue:
    """
    double
    """
    class Node:
        def __init__(self, element, prev, mNext):
            self._element =element
            self._prev = prev
            self._next = mNext

    def __init__(self):
        self._head = self.Node(None, None, None)
        self._tail = self.Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size


    def is_empty(self):
        return self._head._next is None


    def head(self):
        return self._head._element

    def tail(self):
        return self._tail._element

    def enqueue(self, element):
        """
        앞으로 저장함
        1. 새로운 데이터의 next는 head(첫번째 데이터)와 동일한것을 본다
        2. head는 mData를 본다
        3. size += 1
        :param element: 데이터
        :return:
        """
        mData = self.Node(element, self._head, None)
        # 가장 마지막 next는 비어있음
        if self.is_empty():
            self._head._next = mData
            mData._next = self._tail
            self._tail._prev = mData
        else :
            self._head._next._prev = mData
            mData._next =self._head._next
            self._head._next = mData

        self._size += 1


    def dequeue(self):
        """
        tail이 보고 있는것을 삭제
        1. head에서 타고 들어가서 tail -1 을 찾는다
        2. 1의 next를 삭제
        3. tail 이 1을 저장하고
        4. tail.next를 삭제함
        5. size -= 1
        :return:
        """
        if self.is_empty():
            raise EmptyLinked

        dele = self._tail._prev
        res = copy.deepcopy(dele._element)
        self._tail._prev._prev._next = self._tail
        self._tail.prev = self._tail._prev._prev
        del dele
        self._size -= 1
        return res

    def print_list(self):
        """
        list내의 모든 내용을 출력함
        :return:
        """
        cur = self._head
        while cur._next:
            print(cur._element)
            cur = cur._next
        print(cur._element, "\nlast")

    def is_empty(self):
        return self._size == 0


    def end(self):
        return self._head._next._element

    def front(self):
        return self._tail._prev._element

class Tree:

    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            raise NotImplementedError('must be implemented by subclass')

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self,p ):
        raise NotImplementedError('must be implemented by subclass')

    def children(self,p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self,p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children() == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf())

    def _height2(self):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2()

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        return self.preorder()

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield  p

    def _subtree_preorder(self, p):
        yield  p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield  other
        yield  p

    def breadthfirst(self):
        scheduling = list()
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                scheduling.append(p)
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
        # return scheduling