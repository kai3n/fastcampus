from Seungkwon.array_stack import makeStack
#--------------------- 강사님이 제공한 코드 ----------------------------

class Empty(Exception):
    pass

class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head._element              # front aligned with head of list

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as queue is empty
      self._tail = None                     # removed head had been the tail
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)            # node will be new tail node
    if self.is_empty():
      self._head = newest                   # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest                     # update reference to tail node
    self._size += 1


class Tree:
  """Abstract base class representing a tree structure."""

  #------------------------------- nested Position class -------------------------------
  class Position:
    """An abstraction representing the location of a single element within a tree.

    Note that two position instaces may represent the same inherent location in a tree.
    Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
    equivalence of positions.
    """

    def element(self):
      """Return the element stored at this Position."""
      raise NotImplementedError('must be implemented by subclass')

    def __eq__(self, other):
      """Return True if other Position represents the same location."""
      raise NotImplementedError('must be implemented by subclass')

    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)            # opposite of __eq__

  # ---------- abstract methods that concrete subclass must support ----------
  def root(self):
    """Return Position representing the tree's root (or None if empty)."""
    raise NotImplementedError('must be implemented by subclass')

  def parent(self, p):
    """Return Position representing p's parent (or None if p is root)."""
    raise NotImplementedError('must be implemented by subclass')

  def num_children(self, p):
    """Return the number of children that Position p has."""
    raise NotImplementedError('must be implemented by subclass')

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    raise NotImplementedError('must be implemented by subclass')

  def __len__(self):
    """Return the total number of elements in the tree."""
    raise NotImplementedError('must be implemented by subclass')

  # ---------- concrete methods implemented in this class ----------
  def is_root(self, p):
    """Return True if Position p represents the root of the tree."""
    return self.root() == p

  def is_leaf(self, p):
    """Return True if Position p does not have any children."""
    return self.num_children(p) == 0

  def is_empty(self):
    """Return True if the tree is empty."""
    return len(self) == 0

  def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))

  def _height1(self):                 # works, but O(n^2) worst-case time
    """Return the height of the tree."""
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

  def _height2(self, p):                  # time is linear in size of subtree
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height2(c) for c in self.children(p))

  def height(self, p=None):
    """Return the height of the subtree rooted at Position p.

    If p is None, return the height of the entire tree.
    """
    if p is None:
      p = self.root()
    return self._height2(p)        # start _height2 recursion

  def __iter__(self):
    """Generate an iteration of the tree's elements."""
    for p in self.positions():                        # use same order as positions()
      yield p.element()                               # but yield each element

  def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.preorder()                            # return entire preorder iteration

  def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_preorder(self.root()):  # start recursion
        yield p

  def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p                                           # visit p before its subtrees
    for c in self.children(p):                        # for each child c
      for other in self._subtree_preorder(c):         # do preorder of c's subtree
        yield other                                   # yielding each to our caller

  def postorder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_postorder(self.root()):  # start recursion
        yield p

  def _subtree_postorder(self, p):
    """Generate a postorder iteration of positions in subtree rooted at p."""
    for c in self.children(p):                        # for each child c
      for other in self._subtree_postorder(c):        # do postorder of c's subtree
        yield other                                   # yielding each to our caller
    yield p                                           # visit p after its subtrees

  def breadthfirst(self):
    """Generate a breadth-first iteration of the positions of the tree."""
    if not self.is_empty():
      fringe = LinkedQueue()             # known positions not yet yielded
      fringe.enqueue(self.root())        # starting with the root
      while not fringe.is_empty():
        p = fringe.dequeue()             # remove from front of the queue
        yield p                          # report this position
        for c in self.children(p):
          fringe.enqueue(c)              # add children to back of queue

class BinaryTree(Tree):
  """Abstract base class representing a binary tree structure."""

  # --------------------- additional abstract methods ---------------------
  def left(self, p):
    """Return a Position representing p's left child.

    Return None if p does not have a left child.
    """
    raise NotImplementedError('must be implemented by subclass')

  def right(self, p):
    """Return a Position representing p's right child.

    Return None if p does not have a right child.
    """
    raise NotImplementedError('must be implemented by subclass')

  # ---------- concrete methods implemented in this class ----------
  def sibling(self, p): # 형제를 알려주는 메소드
    """Return a Position representing p's sibling (or None if no sibling)."""
    parent = self.parent(p)
    if parent is None:                    # p must be the root
      return None                         # root has no sibling
    else:
      if p == self.left(parent):
        return self.right(parent)         # possibly None
      else:
        return self.left(parent)          # possibly None

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)

  def inorder(self):
    """Generate an inorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_inorder(self.root()):
        yield p

  def _subtree_inorder(self, p):
    """Generate an inorder iteration of positions in subtree rooted at p."""
    if self.left(p) is not None:          # if left child exists, traverse its subtree
      for other in self._subtree_inorder(self.left(p)):
        yield other
    yield p                               # visit p between its subtrees
    if self.right(p) is not None:         # if right child exists, traverse its subtree
      for other in self._subtree_inorder(self.right(p)):
        yield other

  # override inherited version to make inorder the default
  def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.inorder()                 # make inorder the default

class LinkedBinaryTree(BinaryTree):
  """Linked representation of a binary tree structure."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a node."""
    __slots__ = '_element', '_parent', '_left', '_right' # streamline memory usage

    def __init__(self, element, parent=None, left=None, right=None):
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right

  #-------------------------- nested Position class --------------------------
  class Position(BinaryTree.Position):
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node

    def element(self):
      """Return the element stored at this Position."""
      return self._node._element

    def __eq__(self, other):
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

  #------------------------------- utility methods -------------------------------
  def _validate(self, p):
    """Return associated node, if position is valid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._parent is p._node:      # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    """Return Position instance for given node (or None if no node)."""
    return self.Position(self, node) if node is not None else None
    # if node가 None이면  앞을 리턴하고 else이면 None을 리턴해라

  #-------------------------- binary tree constructor --------------------------
  def __init__(self):
    """Create an initially empty binary tree."""
    self._root = None
    self._size = 0

  #-------------------------- public accessors --------------------------
  def __len__(self):
    """Return the total number of elements in the tree."""
    return self._size

  def root(self):
    """Return the root Position of the tree (or None if tree is empty)."""
    return self._make_position(self._root)

  def parent(self, p):
    """Return the Position of p's parent (or None if p is root)."""
    node = self._validate(p)
    return self._make_position(node._parent)

  def left(self, p):
    """Return the Position of p's left child (or None if no left child)."""
    node = self._validate(p)
    return self._make_position(node._left)

  def right(self, p):
    """Return the Position of p's right child (or None if no right child)."""
    node = self._validate(p)
    return self._make_position(node._right)

  def num_children(self, p):
    """Return the number of children of Position p."""
    node = self._validate(p)
    count = 0
    if node._left is not None:     # left child exists
      count += 1
    if node._right is not None:    # right child exists
      count += 1
    return count

  #-------------------------- nonpublic mutators --------------------------
  def _add_root(self, e):
    """Place element e at the root of an empty tree and return new Position.

    Raise ValueError if tree nonempty.
    """
    if self._root is not None:
      raise ValueError('Root exists')
    self._size = 1
    self._root = self._Node(e)
    return self._make_position(self._root)

  def _add_left(self, p, e):
    """Create a new left child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a left child.
    """
    node = self._validate(p)
    if node._left is not None:
      raise ValueError('Left child exists')
    self._size += 1
    node._left = self._Node(e, node)                  # node is its parent
    return self._make_position(node._left)

  def _add_right(self, p, e):
    """Create a new right child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a right child.
    """
    node = self._validate(p)
    if node._right is not None:
      raise ValueError('Right child exists')
    self._size += 1
    node._right = self._Node(e, node)                 # node is its parent
    return self._make_position(node._right)

  def _replace(self, p, e):
    """Replace the element at position p with e, and return old element."""
    node = self._validate(p)
    old = node._element
    node._element = e
    return old

  def _delete(self, p):
    """Delete the node at Position p, and replace it with its child, if any.

    Return the element that had been stored at Position p.
    Raise ValueError if Position p is invalid or p has two children.
    """
    node = self._validate(p)
    if self.num_children(p) == 2:
      raise ValueError('Position has two children')
    child = node._left if node._left else node._right  # might be None
    if child is not None:
      child._parent = node._parent   # child's grandparent becomes parent
    if node is self._root:
      self._root = child             # child becomes root
    else:
      parent = node._parent
      if node is parent._left:
        parent._left = child
      else:
        parent._right = child
    self._size -= 1
    node._parent = node              # convention for deprecated node
    return node._element

  def _attach(self, p, t1, t2):
    """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

    As a side effect, set t1 and t2 to empty.
    Raise TypeError if trees t1 and t2 do not match type of this tree.
    Raise ValueError if Position p is invalid or not external.
    """
    node = self._validate(p)
    if not self.is_leaf(p):
      raise ValueError('position must be leaf')
    if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
      raise TypeError('Tree types must match')
    self._size += len(t1) + len(t2)
    if not t1.is_empty():         # attached t1 as left subtree of node
      t1._root._parent = node
      node._left = t1._root
      t1._root = None             # set t1 instance to empty
      t1._size = 0
    if not t2.is_empty():         # attached t2 as right subtree of node
      t2._root._parent = node
      node._right = t2._root
      t2._root = None             # set t2 instance to empty
      t2._size = 0

if __name__ == "__main__":
    tree = LinkedBinaryTree()
    a = tree._add_root(2)
    b = tree._add_left(a, 7)
    c = tree._add_right(a, 5)
    d = tree._add_left(b, 2)
    e = tree._add_right(b, 6)
    f = tree._add_left(e, 5)
    g = tree._add_right(e, 11)
    h = tree._add_right(c, 9)
    i = tree._add_left(h, 4)

    print("Start ->", end="")
    for a in tree.inorder():
        print(str(a._node._element) + " -> ", end="")
    print("Finish")

de = makeStack()
# 연산자가 두개인경우에는 반드시 괄호로 묵는다
def inorder_to_postorder(exp):
  #inorder -> post로 바꾼다

    operator = "+-*/()"                     # 연산자들을 선언
    result = list()                     # 후위 표기법으로 결과가 저장되는 리스트
    stack = list()                      # list를 스택으로 사용함.

    for symbol in exp:
        if symbol not in operator:          # 숫자일 경우 바로 결과리스트에 넣는다.
            result.append(symbol)
        else:
            if symbol in "+-*/":        # 더하기, 빼기, 곱하기, 나누기 연산자일 경우
                stack.append(symbol)    # 후위 표기법으로 변환하기 위하여 우선 별도 스택에 임시로 저장.
            elif symbol == ")":         # 닫는 괄호 ) 일 경우 저장해 연산자 하나를 결과리스트에 추가한다.
                result.append(stack.pop())      # 이 때 pop()을 통해 스택을 하나 비운다.

    while len(stack) != 0:              # 스택에 남아 있는 연산자들을 pop()으로 하나씩 결과리스트에 붙여주면
        result.append(stack.pop())      # 중위 표기법에서 후위 표기법으로 변환 완료!
    return ''.join(result)

num = "((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))"
postorder = inorder_to_postorder(num) #31+3*95-2+/374-*6+-
reverse = postorder[::-1]
# print("결과",postorder)
# print("거꾸로",reverse)
#---- 1/27


def calculate(postorder_num):
  """
  1. postorder로 들어온 숫자로 계산한다.
  2. 두개의 스택을 선언
  3. 하나는 숫자 하나는 연산자
  4. 각 연산자에 맞는 계산을 실행해야 함
  5. 숫자가 2개, 연산자 1개 이면 연산을 실행한다
  :param postorder_num:
  :return:
  """
  num = makeStack()
  opp = makeStack()
  for n in postorder_num:
    if n.isdigit():#0~9 10진수
      num.push(int(n))
    else:
      opp.push(n) # 무조건 1이다 그러니깐 필요 없다
      print(len(opp))

    if len(num) >= 2 and len(opp) >= 1:
      b = num.pop()
      a = num.pop()
      op = opp.pop()
      if op == "+":
        num.push(a+b)
      elif op == "-":
        num.push(a-b)
      elif op == "*":
        num.push(a*b)
      elif op == "/":
        num.push(a/b)
      # print(a, b, op)
  return int(num.pop())

# print(calculate(postorder))



def rectangle(n):
  res = list()
  for num in range(1, n*n):
    if num % n == 0:
      res.append(num)
    else :
      res.append(0)
  return res


rectangle(4)


