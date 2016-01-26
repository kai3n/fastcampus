
class MyLinkedList:

    class Node:
        def __init__(self):
            self.next = self.Node()
            self.data = object

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def __len__(self):
        return self.size


    def add_first(self, add):
        """
        첫번째에 데이터를 추가한다(head가 가리키는 부분)
        size += 1
        :param add:
        :return:
        """
        mData = self.Node()
        mData.data = add
        mData.next = None # 다음칸의 정보는 없다
        if self.head == None:
            self.head = mData
            # head가 첫 데이터를 봐야 하고
        else:
            self.tail = mData
            # tail은 무조건 마지막 데이터를 봐야한다
        self.size += 1
        # 모든 노트의 next는 현재의 tail을 본다 -> 연결됨

    def add_last(self, add):
        """
        가장 마지막에 있는 데이터를 삭제한다(tail이 가리키는 부분)
        :return:
        """
        if self.head is None or self.tail is None :
            raise linkedListEmpty

        mData = self.Node()
        mData.data = add
        mData.next = None
        self.tail = mData
        # self.tail -> None tail.next는 무조건 none이다
        self.size += 1


    def remove(self):
        """
        head가 가리키고 있는 데이터를 삭제한다
        :return:
        """
        if self.head == None:
            raise linkedListEmpty
            # list각 비어있는 경우
        else:
            mid = self.head.next # 두번째 데이터
            self.head.next = None #첫번째 데이터의 연결선을 끊는다
            self.head = mid #나의 head에 2번째 데이터를 넣는다
            self.size -= 1

    def remove_last(self):
        """
        tail이 가리키고 있는 데이터를 삭제한다
        :return:
        """


class linkedListEmpty(Exception):
    pass