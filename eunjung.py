########################### 과 ####################### 제 #####################################

def wd_upper(word):
    """
    이 함수는 word 문자열(str type) 전체를 대문자로 변환하는 함수이다.
    매개변수가 str 타입이 아닐 시 None을 반환한다.
    ex1) wd_upper('apple')를 호출할 시 'APPLE'를 반환한다.
    ex2) wd_upper('Plane')를 호출할 시 'PLANE'를 반환한다.
    ex3) wd_upper('AbCdE')를 호출할 시 'ABCDE'를 반환한다.
    :param word:
    :return word:
    """
    if type(word) != str:
        return None

    result = ""

    for unit in word:
        num = ord(unit)
        if 96< num < 123:
            num -= 32
        result += chr(num)
    return result



def wd_lower(word):
    """
    이 함수는 word 문자열(str type) 전체를 소문자로 변환하는 함수이다.
    매개변수가 str 타입이 아닐 시 None을 반환한다.
    ex1) wd_upper('apple')를 호출할 시 'apple'를 반환한다.
    ex2) wd_upper('Plane')를 호출할 시 'plane'를 반환한다.
    ex3) wd_upper('AbCdE')를 호출할 시 'abcde'를 반환한다.
    :param word:
    :return word:
    """
    if type(word) != str:
        return

    result = ""

    for unit in word:
        num = ord(unit)
        if 64 < num < 91:
            num += 32
        result += chr(num)
    return result



print(wd_lower('aPplE'))


#############################################################################################





# 1. 문장이 들어오면 해당 문장을 단어별로 끊어, 단어 갯수 리턴
def word_count(word):
    words_list = word.split(" ")
    word_cnt = len(words_list)
    return word_cnt

print(word_count("Return a copy of the string where all tab characters are"\
                +"replaced by one or more spaces, depending on the current column"\
                +"and the given tab size. Tab positions occur every tabsize characters"))


# 2. (문자열, 리스트, 튜플)에 특정 단어가 존재한다면 True 아니면 False 리턴
def search(string, word):

    if type(string) == str:
        new_list = string.split(" ")
    elif type(string) == dict:
        return False
    else:
        new_list = list(string)

    word = str(word).lower()

    for val in new_list:
        val = str(val)
        val = str(val).lower()
        if val == word:
            return True
        else:
            for count in range(0,len(val)):
                length = len(val)
                combine = val[count]
                if combine == word:
                    return True
                else:
                    while True:
                        combine += val[]

    return False

#print(search({'a':'b'}, "COPY"))
print(search([1,2,3,4,5,'apple',], 'a'))



# 3. range 함수 구현!!!!
def make_range(start, end, step):
    # 범위를 구하는 게 가능한 수인지를 확인
    diff = end - start
    if diff*step < 0:
        return "error"

    # 가능한 경우
    start_num = start
    number_list = [start_num]

    while True:
        start_num += step

        if step > 0:
            if start_num < end :
                number_list.append(start_num)
            else:
                break
        else:
            if start_num > end :
                number_list.append(start_num)
            else:
                break

    return number_list


print(make_range(5,-10,-1))


# 4. upper 와 lower










################################160114####################################################################

class Calculator():
    def __init__(self):
        pass

    def add(self, x, y):
        '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        result = int(x + y)
        return result

    def subtract(self, x, y):
        '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        result = float(x - y)
        return result

    def multiply(self, x, y):
        '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        result = int(x*y)
        return result

    def divide(self, x, y):
        '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
        if x == 0 or y == 0:
            return 0

        result = int(x//y)
        remain = 0

        if x*y > 0:
            remain = float(x/y) - float(x//y)
        else:
            remain = float(x/y) - (float(x//y) + 1)

        if float(x//y) > 0:
            if abs(remain) >= 0.5:
                result += 1
        else:
            if abs(remain) >= 0.5:
                result = float(x//y)
            else:
                result = float(x//y) + 1

        return result

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

> > > calc = Calculator()
> > > calc.add(1,2)
> > > calc.subtract(3,2)














