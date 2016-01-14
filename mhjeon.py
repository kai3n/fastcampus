# '''
# sentence = "I am a boy"
#
# def word_count(sentence):
#     return len(sentence.split())
#
# print(word_count(sentence))
#
# #####################################################################################################################
# string1 = "I am a boy"
# string2 = ["I", "am", "a", "boy"]
# string3 = ("I", "am", "a", "boy")
# string4 = {"I" : "am", "a" : "boy"}
# string5 = [1,2,'abc',0.1,'efd']
#
# def search(input, word_or_character):
#     if type(input) == str:
#         if str(word_or_character) in input:
#             return True
#     elif type(input) == tuple or type(input) == list:
#         empty_string = ""
#         for element in input:
#             empty_string += str(element)
#         if word_or_character in empty_string:
#             return True
#     return False
#
# print(search(string5, "bc"))
#
# #####################################################################################################################
# def range_func(input, start, end, step):
#     index = start - 1
#     element_list = []
#
#     if start >= 0:
#         while index < end:
#             element_list.append(input[index])
#             index += step
#         return element_list
#
#     # Todo: backward range functino yet to be coded
#     else:
#         index = len(input) + start
#         while index < end:
#             element_list.append(input[index])
#             index += step
#         return element_list
#
# input = "123456789"
# print(range_func(input, -1, -5, -2))
#
# #####################################################################################################################
#
# def print_args(*args):
#     print("Positional argument tuple:", args)
#
# print_args("adfasdf","Asdfasdf","asdfasdfasdf")
#
# def print_kwargs(**kwargs):
#     print('Keyword arguements:',kwargs)
#
# print_kwargs(wine="merlot", entree='mutton', dessert='macaroon')
#
# #####################################################################################################################
#
# def answer():
#     print(42)
#
# answer()
#
# def run_something(func):
#     func()
#
# run_something(answer)
#
# ######################################################################################################################
# animal = "fruitbat"
#
# def change_and_print_global():
#     #global animal
#     animal = "wormbat"
#     print("inside chang_and_print_global:", animal)
#
# print(animal)
# change_and_print_global()
# print(animal)
#
# ######################################################################################################################
# #
# # 14일 목요일: 퀴즈 문제
# #
# def reverse_word(word):
#     if len(word)<=0:
#         print ("No word")  ####redundant & 프린트와 return None이 둘 다 반환 -> return "No word"로 두 줄을 한 줄로 줄일 수 있겠다
#         return None
#     else:
#         empty_word = ""
#         for char in word[::-1]:
#             empty_word += char
#         word = empty_word
#         return word
#
# print(reverse_word(""))
# '''
#
# ######################################################################################################################
# # 날짜: 2016.1.14
# # 과제: upper() & lower() 구현
# # 내용: upper()와 lower()는 string class의 method이다. 문자열 객체가 method를 호출하면, 각각 대문자와 소문자로 변환한다.
# #      파라미터가 string이 아닌 경우에는 attributeError가 발생한다. 정확한 구현을 위해서는 string class 구현과 try-catch 구문을 사용해야 한다.
#
# def change_to_upper(word):
#     #인자로 받는 word가 문자열인 경우에만 함수를 실행한다.
#     if type(word) != str:
#         return "올바른 입력값이 아닙니다."
#     #올바른 형태의 인자가 들어왔을 경우만 변환 진행한다.
#     else:
#         uppered_word = ""
#         for character in word:
#             #소문자는 ASCII 코드상 97-122에, 대문자는 65-90에 해당한다. 같은 글자의 소문자 - 대문자의 차이는 32이다.
#             #함수 ord()는 글자를 해당 ASCII코드 숫자로, chr()는 ASCII 코드를 글자로 변환한다.
#             ascii_char = ord(character)
#             if ascii_char >= 97 and ascii_char <= 122:
#                 character = chr(ascii_char - 32)
#             uppered_word += str(character)
#         return uppered_word
#
# #Change_to_upper()의 코드를 살짝 바꾸면 된다
# def change_to_lower(word):
#     if type(word) != str:
#         return "올바른 입력값이 아닙니다."
#     else:
#         lowered_word = ""
#         for character in word:
#             #소문자는 ASCII 코드상 97-122에, 대문자는 65-90에 해당한다. 같은 글자의 소문자 - 대문자의 차이는 32이다.
#             #함수 ord()는 글자를 해당 ASCII코드 숫자로, chr()는 ASCII 코드를 글자로 변환한다.
#             ascii_char = ord(character)
#             if ascii_char >= 65 and ascii_char <= 90:
#                 character = chr(ascii_char + 32)
#             lowered_word += str(character)
#         return lowered_word
#
# test_string1 = "abBzrTsdf134"
# test_string2 = 1234
#
# print(change_to_upper(test_string1))
# print(change_to_upper(test_string2))
# print(change_to_lower(test_string1))
# print(change_to_lower(test_string2))
#
# ######################################################################################################################
# '''
# def countdown(n):
#     print('counting down from %d' %n)
#     while n > 0:
#         yield n
#         n -= 1
#     return
#
# print(type(countdown))
# '''
# ######################################################################################################################

import time

def elapsed_time(functor):
    def decorated(*args, **kwargs):
        start=time.time()
        functor(*args,**kwargs)
        end=time.time()
        print("Elapsed time:%f" % (end-start))
    return decorated

@elapsed_time
def hello():
    print("Hello")

hello()

print(locals())
print(globals())

# ######################################################################################################################

class Calculator():
    def __init__(self):
        pass
    def add(self, x, y):
        '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return x + y
    def subtract(self, x, y):
        '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return float(x - y)
    def multiply(self, x, y):
        '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return x * y
    def divide(self, x, y):
        '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
        split_num = str(x/y).split(".")
        num = int(split_num[0])
        digit_to_compare = int(split_num[1][0])

        if digit_to_compare >= 5:
            return num +1

        return num

    def expCalc(self,expStr):
        """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 20을 반환한다.
        ex) expCalc('1+3+5-0')는 9을 반환한다.
        ex) expCalc('4+3+5/3')는 4을 반환한다.
        """

        '''
        ints=[]
        cal_ints = []_
        ops=[]
        digit=0
        sum = 0

        for element in expStr:
            if type(element) == int:
                integers += element
                digit += 1
            else:

                for i in range(len(integers))
                digit = 0
        return
        '''

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
calc.subtract(3,2)
print(calc.multiply(4,3))
print(calc.divide(18,5))
