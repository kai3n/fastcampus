class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        # len 함수를 써서 그래도 int 형 변수로 반환
        length = len(self.data)

        print(length)
        #  return length
    def is_empty(self):
        # List 에 값이 있으면 False 없으면 True를 반환한다
        if self.data:
            print(False)
            #return False
        else:
            print(True)
            #return True

    def push(self,e):
        # append 해서 Stack 맨 위에 올려놓는 것처럼 구사
        self.data.append(e)

    def top(self):
        # 리스트 맨 뒤 숫자를 가리키게하고 str로 변화시켰다
        top_value = str(self.data[len(self.data)-1])
        print("Top Value is",top_value)
        #return = top_value
    def pop(self):
        # pop에서 length 의 길이를 줄인다
        if self.data:

            pop_length = len(self.data) -1
            print(self.data[pop_length],"is deleted")
            del self.data[pop_length]

        else:
            print("error")




S = ArrayStack()
S.push(5)
S.push(3)
S.__len__()
S.pop()
S.is_empty()
S.pop()
S.is_empty()
S.push(7)
S.push(9)
S.top()
S.push(4)
S.__len__()
S.pop()
S.push(6)
S.push(8)
S.pop()