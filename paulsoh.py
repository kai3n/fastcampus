test_list = [1,2,'abc', 0.1, 'efd']
query_for_test_list = 'bc'



def search(sentance, word):
    if type(sentance) == str and type(word) == str:
        if word in sentance:
            return True
    elif type(sentance) == tuple or type(sentance) == list:
        for i in range(0,len(sentance)):
            if type(sentance[i]) == int or type(sentance[i]) == float:
                if sentance[i] == word:
                    return True
            elif word in sentance[i]:
                return True
    return False

def word_count(word):
    return len(word.split())

def range_function(a, *args):
    a = int(a)
    result = []
    counter = 0
    if len(args) == False:
        if a > 0:
            while(counter < a):
                result.append(counter)
                counter += 1
            return result
        elif a < 0:
            while(counter > a):
                result.append(counter)
                counter -= 1
            return result
        else:
            return False

    elif len(args) == 1:
        if a < args[0]:
            counter = a
            while(counter < args[0]):
                result.append(counter)
                counter += 1
            return result
        elif a > args[0]:
            counter = a
            while(counter > args[0]):
                result.append(counter)
                counter -= 1
            return result
        else:
            return False

    elif len(args) == 2:
        counter = a
        if a < args[0]:
            while(counter < args[0]):
                if args[1] < 0:
                    return False
                result.append(counter)
                counter += args[1]
            return result
        elif a > args[0]:
            while(counter > args[0]):
                if args[1] > 0:
                    return False
                result.append(counter)
                counter += args[1]
            return result
        else:
            return False
    else:
        return False

# A = 65 a = 97 Z = 90 z = 122

################################################################################################
###  wd_lower fucntion ; takes str as input and lower cases all the letters inside the str  ###
################################################################################################
def wd_lower(string):
    buf = ''
    if string is None :
        return buf
    for char in string:
        if ord('A') <= ord(char) <= ord('Z'): # Upper case character
            buf += chr(ord(char)+32)
        else:
            buf += char
    return buf
############################################################################################

################################################################################################
###  wd_upper fucntion ; takes str as input and upper cases all the letters inside the str  ###
################################################################################################
def wd_upper(string):
    buf = ''
    if string is None :
        return buf
    for char in string:
        if ord('a') <= ord(char) <= ord('z'): # Upper case character
            buf += chr(ord(char)-32)
        else:
            buf += char
    return buf
############################################################################################


## test / debugging sequence ##

print(wd_lower('heLLo mY namE iS Paul soh'))
print(wd_upper('heLLo mY namE iS Paul soh d8d7Cdf7gFddvDDF'))



# print(range_function(5))
# print(range_function(-5))
# print(range_function(0))
#
# print(range_function(10,7))
# print(range_function(11,22))
#
# print(range_function(0,10,2))
# print(range_function(0,10,-2))
# print(range_function(0, -10, -2))


test_string = 'what is my name my name is paul soh hello world'
query_for_test_string = 'name'



test_dict = {'a':'b', 'c':'d'}
query_for_test_dict = 'a'

# print(search(test_list, query_for_test_list))
# print(search(test_string, query_for_test_string))
# print(search(test_dict, query_for_test_dict))

print(wd_lower('aBcDeFgHiJ'))


class Calculator():
    def __init__(self):
        pass
    def add(self, x, y):
        return int(x + y)
        '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
    def subtract(self, x, y):
        '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return float(x-y)
    def multiply(self, x, y):
        '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return int(x * y)
    def divide(self, x, y):
        '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
        real_ans = int(x/y)
        ans = str(float(x/y))
        if len(ans)>= 3:
            if int(ans[2]) >= 5:
                return real_ans+1
            else:
                return real_ans
        return real_ans

    def expCalc(self,expStr):
        """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 20을 반환한다.
        ex) expCalc('1+3+5-0')는 9을 반환한다.
        ex) expCalc('4+3+5/3')는 4을 반환한다.
        """
        operands = []
        operand2 = ''
        operators = []
        buf = []
        def isCharOperator(char):
            if char is '+':
                return '+'
            elif char is '-':
                return '-'
            elif char is '*':
                return '*'
            elif char is '/':
                return '/'
            else:
                return False

        for element in expStr:
            if isCharOperator(element) != False:
                operators.append(element)
                print(operators)
            buf += element
            print(buf)

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
# print(calc.add(1,2))
# print(calc.subtract(3,2))
# print(calc.multiply(3,5))
print(calc.divide(3,5))
print(calc.divide(2,5))
print(calc.divide(100,99))
print(calc.divide(50,99))
print(calc.divide(49,100))


#print(calc.expCalc('123-442+5221'))



