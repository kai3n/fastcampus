
#TODO:upper, lower 과제,#
#제출합니다

def new_upper(string):
    if type(string) == str:
        pass
    else:
        return None
    chars = ''
    for char in string:
        asci = ord(char)
        if 96 < asci and asci < 123:
            asci -= 32
            chars += chr(asci)
        elif 64 < asci and asci < 91 or asci == 32:
            chars += chr(asci)
        else:
            return 'arg must be only str'
    return chars

print(new_upper('PlAnRi abLUeu'))

def new_lower(string):
    chars = ''
    for char in string:
        asci = ord(char)
        if 64 < asci and asci < 91:
            asci += 32
            chars += chr(asci)
        elif 96 < asci and asci < 123 or asci == 32:
            chars += chr(asci)
        else:
            return 'arg must be only str'
    return chars

print(new_lower('SuPeR PoWeR'))


# class Calculator():
#     def __init__(self):
#         pass
#     def add(self, x, y):
#         self.x = x
#         self.y = y
#         return int(self.x + self.y)
#     def subtract(self, x, y):
#         #self.x = x
#         #self.y = y
#         return float(x - y)
#     def multiply(self, x, y):
#         return int(x * y)
#     def divide(self, x, y):
#         value = x / y
#
#         if x > 0 and y > 0:




        # value = x / y
        # differ = value - int(value)
        # fill = 1 - differ
        #
        # if x >= y:
        #     if differ >= 0.5:
        #         return int(value + fill)
        #     else:
        #         return int(value - differ)
        # else:
        #     if differ <= 0.5:
        #         return int(value - differ)
        #     else:
        #         return int(value + fill)

#     def expCalc(self,expStr):
#         """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
#         ex) expCalc('1+3-5')는 -1을 반환한다.
#         ex) expCalc('1+3*5')는 20을 반환한다.
#         ex) expCalc('1+3+5-0')는 9을 반환한다.
#         ex) expCalc('4+3+5/3')는 4을 반환한다.
#         """
#         # numList = []
#         # intList = []
#         # calList = []
#         # for char in expStr:
#         #
#         # return
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
# calc = Calculator()
# # calc.expCalc('1+2+3')
# print(calc.add(-4,3))
# print(calc.subtract(-5.5,-3.1))
# print(calc.divide(-2,3))

#
# #######################################################################Before 01/14
# import time
#
#
# def elapsed_time(functor):
#     def decorated(*args,**kwargs):
#         start = time.time()
#         functor(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         result = functor(*args, **kwargs)
#         return result
#     return decorated
#
#
# @elapsed_time
# def word_count(word):
#     word_cnt = 0
#     words = str(word)
#     word_cnt = len(words.split(' '))
#     return word_cnt
#
# print(word_count(' sd s sd sd sd '))
#
# @elapsed_time
# def search(string, word):
#     if type(string) == str:
#         if word in string:
#             return True
#         else:
#             return False
#     elif type(string) == list or type(string) == tuple:
#         if type(word) == str:
#             strings = []
#             for item in string:
#                 if type(item) == str:
#                     strings.append(item)
#                 else:
#                     continue
#             for checkStr in strings:
#                 if word in checkStr:
#                     return True
#                 else:
#                     continue
#             return False
#
#         elif type(word) == int:
#             integers = []
#             for item in string:
#                 if type(item) == int:
#                     integers.append(item)
#                 else:
#                     continue
#             for checkInt in integers:
#                 if word in integers:
#                     return True
#                 else:
#                     continue
#             return False
#
#         elif type(word) == float:
#             floats = []
#             for item in string:
#                 if type(item) == float:
#                     floats.append(item)
#                 else:
#                     continue
#             for checkFloat in floats:
#                 if word == checkFloat:
#                     return True
#                 else:
#                     continue
#             return False
#
#     else:
#         return 'Type Error'
#
# print(search(['apple', 1, 0.1, 8,4,123,566,885,3289,4654684,645654,21,3,21,8,65, 0.4,'power'], 0.3))
#
# def num_range(start, end, step):
#     num_list = []
#     if step == 0:
#         return 'error: step must not be Zero'
#     elif step > 0:
#         if start < end:
#             while start < end:
#                 num_list.append(start)
#                 start += step
#             return num_list
#         else:
#             return []
#     elif step < 0:
#         if start > end:
#             while start > end:
#                 num_list.append(start)
#                 start += step
#             return num_list
#         else:
#             return []
#     else:
#         return 'Unknown Error'
#
# print(num_range(22, 22, 1))



