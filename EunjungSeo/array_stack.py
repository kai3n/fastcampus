class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self.data = []
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        # 리스트가 비어있다면 True
        length = len(self.data)
        if length == 0:
            return True
        else:
            return False

    def push(self, e):
        # 리스트에 데이터 넣기
        self.data.append(e)
        self.count += 1


    def top(self):
        # 가장 마지막에 들어간 수가 무엇인지 알려준다
        length = len(self.data) - 1
        if length >= 0:
            return self.data[length]
        else:
            raise Empty("error")

    def pop(self):
        # 가장 마지막에 들어있는 데이터를 빼서 반환
        length = len(self.data) - 1
        if length >= 0:
            self.count -= 1
            return self.data.pop(length)
        else:
            raise Empty("error")
