"""
word count

def world_count(word):
    word_cnt = word.count(' ') + 1
    return word_cnt

print(world_count('i am a crazy dog 그래 미친개 맞아 미친개'))

def word_count1(word1):
    word_cnt1 = len(word1.split(' '))
    return word_cnt1

print(word_count1('i am a crazy dog. 그래 미친개 맞아 미친개'))

search

def a_search ( target , word ):

    if type(target) == dict:
        return False

    elif type(target) == list:
        target5 = list()
        for i in target:
            target5.append(str(i))
        target_string=','.join(target5)
        a_find= target_string.count(word)
        return bool(a_find)

    else:
        a_find= target.count(word)
        return bool(a_find)

target1 = { 'a': 'b', 'c' : 'd'}
target2 = 'abc'
target3 = ['a','bc','d']
target4 = [1,2,'abc',0.1,'efd']

word1 = 'a'
word2 = 'ab'
word3 = 'd'
word4 = 'e'

print(a_search(target4, word4))

"""

# def ran(a,b,c):
#     if type(a and b and c) == int:
#         e_list = []
#         while a < b:
#             if c <= 0:
#                 return "can`t calculating"
#             e_list.append(a)
#             a = a + c
#         else a > b :
#              if c >= 0:
#                 return "can`t calculating"
#             e_list.append(a)
#             a = a + c
#         else:
#             return "can`t calculating"
#     else:
#         return "not range function"
#
# print (ran(20, 28, 4))

class Calculator():
    def __init__(self):
        pass
    def add(self, x, y):
        self.plus = int(x + y)
        '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return self.plus

    def subtract(self, x, y):
        self.minus = float( x - y )
        '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return self.minus

    def multiply(self, x, y):
        self.multiple = int (x*y)
        '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return  self.multiple

    def divide(self, x, y):

        '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
        return
    def expCalc(self,expStr):
        """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 20을 반환한다.
        ex) expCalc('1+3+5-0')는 9을 반환한다.
        ex) expCalc('4+3+5/3')는 4을 반환한다.
        """
        return
    def expCalcAdvanced(self,expStr):
        """숫자 표현식을 문자열로 받아서(이 때 *와 / 연산자는 우선순위로 계산함, ()괄호에 대한 우선순위도 매김)표현식에
        대한 결과를 소수점 둘째자리에서 반올림하여 실수형으로 변환하는 함수이다. 난이도:★★★★★
        여기까지 실습시간 내에 완성하시는분은 제가 소고기 사드립니다.

        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 16을 반환한다.
        ex) expCalc('100+3+5-0')는 108을 반환한다.
        ex) expCalc('(100+3)*5+300-(200+10)/2')는 710을 반환한다.
        ex) expCalc('4+3+5/3')는 8.67을 반환한다.
        """
        return

calc = Calculator()
print(calc.add(1,2))
print(calc.subtract(3,2))
print(calc.multiply(5,2))
