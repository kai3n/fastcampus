
class Empty(Exception):       #클래스 Exception에 포함된 함수들을 class Empty가 그기능들을 포함한다.
    pass

class ArrayStack:           #?왜 클래스를 위에 아래 두개선언했는지

    def __init__(self):                      #스택 객체를 만들었을때 만들자마자 나오는 생성자함수 이때 self 는 객체가 나올 자리
        self._data = []                  #생성자함수의 기본값이 self._data 가 빈리스트다.

    def __len__(self):
        return len(self._data)      #셀프데이터의 길이를 반환한다.

    def is_empty(self):
        if len(self._data) == 0:    #self.data 의길이가 0일떄 True 를 반환 아니면 False를 반환

            return True
        else:
            return False

    def push(self, e):
        self._data.append(e)   #빈리스트 가장 뒤에 e라는 엘리먼트를 더하하하함

    def top(self):
        if self.is_empty():
            raise Empty    # 만약 리스트가 빈리스트일 때 오류를 발생시키겠다.
        else :
            return self._data[-1] # 데이터의 -1 인텐트를 리턴한다.

    def pop(self):
        if self.is_empty():         #만약 리스트가 비어있으면 raise 오류띄우고 안비어있으면 pop()을써서 마지막리스트를 리턴하고 삭제한다.
            raise Empty
        else:
            return self._data.pop()


AS = ArrayStack()


print(len(AS))
print(AS.__len__())
print(AS.is_empty())
print(AS._data.append(2))
print(AS._data.append(3))
print(AS._data)
print(AS._data[-1])
print(AS._data.pop())
print(AS._data)