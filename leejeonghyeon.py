# class Calculator():
#     def __init__(self):
#         pass
#     def add(self, x, y):
#         '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
#         return
#     def subtract(self, x, y):
#         '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
#         return
#     def multiply(self, x, y):
#         '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
#         return
#     def divide(self, x, y):
#         '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
#         return
#     def expCalc(self,expStr):
#         """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
#         ex) expCalc('1+3-5')는 -1을 반환한다.
#         ex) expCalc('1+3*5')는 20을 반환한다.
#         ex) expCalc('1+3+5-0')는 9을 반환한다.
#         ex) expCalc('4+3+5/3')는 4을 반환한다.
#         """
#         return
#     def expCalcAdvanced(self,expStr):
#         """숫자 표현식을 문자열로 받아서(이 때 *와 / 연산자는 우선순위로 계산함, ()괄호에 대한 우선순위도 매김)표현식에
#         대한 결과를 소수점 둘째자리에서 반올림하여 실수형으로 변환하는 함수이다. 난이도:★★★★★
#         여기까지 실습시간 내에 완성하시는분은 제가 소고기 사드립니다.
#
#         ex) expCalc('1+3-5')는 -1을 반환한다.
#         ex) expCalc('1+3*5')는 16을 반환한다.
#         ex) expCalc('100+3+5-0')는 108을 반환한다.
#         ex) expCalc('(100+3)*5+300-(200+10)/2')는 710을 반환한다.
#         ex) expCalc('4+3+5/3')는 8.67을 반환한다.
#         """
#         return
#
class Calculator():

    def __init__(self):
        pass

    def add(self, x, y):
        #'두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return int(x+y)
    def subtract(self, x, y):
        #'두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return float(x-y)
    def multiply(self, x, y):
        #'두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return int(x*y)
    def divide(self, x, y):
        #'두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
        divXy = x//y
        if (x%y)/y >=0.5:
            divXy= x//y+1
        return divXy
    def expCalc(self,expStr):
        """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 20을 반환한다.
        ex) expCalc('1+3+5-0')는 9을 반환한다.
        ex) expCalc('4+3+5/3')는 4을 반환한다.
        """
        return

#     def expCalcAdvanced(self,expStr):
#         """숫자 표현식을 문자열로 받아서(이 때 *와 / 연산자는 우선순위로 계산함, ()괄호에 대한 우선순위도 매김)표현식에
#         대한 결과를 소수점 둘째자리에서 반올림하여 실수형으로 변환하는 함수이다. 난이도:★★★★★
#         여기까지 실습시간 내에 완성하시는분은 제가 소고기 사드립니다.
#
#         ex) expCalc('1+3-5')는 -1을 반환한다.
#         ex) expCalc('1+3*5')는 16을 반환한다.
#         ex) expCalc('100+3+5-0')는 108을 반환한다.
#         ex) expCalc('(100+3)*5+300-(200+10)/2')는 710을 반환한다.
#         ex) expCalc('4+3+5/3')는 8.67을 반환한다.
#         """
#         return




calc = Calculator()
print(calc.add(1,2))
print(calc.subtract(3,2))
print(calc.multiply(4,6))
print(calc.divide(9,7))
print(calc.expCalc(4+3+5/3))

#=========================================================================================

# def main():
#     # print(word_count("프로그래밍이란 컴퓨터에 인간이 생각하는 것을 입력시키는 행위라고 할 수 있다."))#10
#     #
#     # print(word_search({'a':'b','c':'d'},'c'))#true
#     # print(word_search({'a':'b','c':'d'},'u'))#false
#     # print(word_search([1,2,'abc',0.1,'efd'],'ab')) #true
#     # print(word_search([1,2,'abc',0.1,'efd'],'aaa'))#false
#
#     # print(make_range(1,10,1))
#     # print(make_range(10,1,-1))
#     # print(make_range(-10,1,2))수정하기
#     print(wd_upper("abcDefG"))
#
# ##Count
# def word_count(word):
#     count_cnt =len(list(word.split()))
#     return count_cnt
#
# ##Search
# def word_search(w01, w02):
#
#     if type(w01)==dict:                     ##딕셔너리
#         for w01_key in w01.keys():
#             if w01_key==w02:
#                 return True
#             return False
#
#     elif type(w01)==list:                   ##리스트
#         w02_str =''
#         i=1
#         for i in w01:
#             w02_str += str(i)
#         #print(w02_str)
#
#         if w02 in w02_str:
#             return True
#         return False
#
#     else:
#         print("기타...")
#
# def make_range(s_num,e_num,j_idx):
#     r_far = e_num+(s_num*-1)
#
#     if r_far>=0:
#         r_far = r_far
#     else:
#         r_far = r_far * -1
#
#     r_result = list()
#     i = 0
#     while r_far!=i:
#         r_result.append(s_num)
#         s_num += j_idx
#         i += 1
#         if s_num==e_num:#수정중
#             break
#
#     return r_result
#
# def wd_upper(word):
#     list_upper = list()
#     #65~90까지 대문자
#     i=ord("A")
#     while True:
#         list_upper.append(i)
#         i += 1
#         if i > ord("Z"):
#             break
#     ws = list(word)
#     #print(list_upper)
#
#     # j=0 ~ len(ws)까지
#     j=0
#     while True:
#         if ord(ws[i]) in list_upper:
#             #print("test")
#             pass
#         else:
#             ws.insert(j,int(j+1))
#         j += 1
#         if j>=len(ws):
#             break

# import time
#
# def elapsed_time(functor):
# 	def decorated(*args, **kwargs):
# 		start = time.time()
# 		functor(*args, **kwargs)
# 		end = time.time()
# 		print(end-start)
# 	return decorated
#
# @elapsed_time
# def hello():
#
# 	print(locals())
#
#
# hello()




 #     """
 # +    이 함수는 word 문자열(str type) 전체를 대문자로 변환하는 함수이다.
 # +    매개변수가 str 타입이 아닐 시 None을 반환한다.
 # +    ex1) wd_upper('apple')를 호출할 시 'APPLE'를 반환한다.
 # +    ex2) wd_upper('Plane')를 호출할 시 'PLANE'를 반환한다.
 # +    ex3) wd_upper('AbCdE')를 호출할 시 'ABCDE'를 반환한다.
 # +    :param word:
 # +    :return word:
 # +    """

#  +def wd_lower(word):
#  +    """
#  +    이 함수는 word 문자열(str type) 전체를 소문자로 변환하는 함수이다.
#  +    매개변수가 str 타입이 아닐 시 None을 반환한다.
#  +    ex1) wd_upper('apple')를 호출할 시 'apple'를 반환한다.
#  +    ex2) wd_upper('Plane')를 호출할 시 'plane'를 반환한다.
#  +    ex3) wd_upper('AbCdE')를 호출할 시 'abcde'를 반환한다.
#  +
#  +    :param word:
#  +    :return word:
#  +    """
# # pass
