
"""
def word_count(word):
    word_cnt=word.split(" ")

    return len(word_cnt)

print (word_count('I am a boy'))


def search(string, word):
"""

"""
    if type(string) == list or type(string) == tuple or type(string) ==set or type(string)==str:
        mon = list(string)
        if word in mon:
            return True
        else:
            return False

    else :
        return False




print(search({1,2},1))
print(search((1,2),1))
print(search('aaa','a'))
print(search('afefa','a'))
"""
"""
def word_upper(word):
    if type(word)==str:
        word_up = list(word)
        word_ascii = []
        for i in word_up:
            trans_ascii = ord(i)
            word_ascii.append(trans_ascii)

        last_word_list = []
        for i in word_ascii:
            if i>=65 and i<=90:
                trans_word = chr(i)
                last_word_list.append(trans_word)
            else:
                trans_word = chr(i-32)
                last_word_list.append(trans_word)
    else:
        return False

    last_string=""
    for the_last in last_word_list:
        last_string += str(the_last)

    return last_string





def word_lower(word):
    if type(word)==str:
        word_up = list(word)
        word_ascii = []
        for i in word_up:
            trans_ascii = ord(i)
            word_ascii.append(trans_ascii)

        last_word_list = []
        for i in word_ascii:
            if i>=97 and i<=122:
                trans_word = chr(i)
                last_word_list.append(trans_word)
            else:
                trans_word = chr(i+32)
                last_word_list.append(trans_word)

    else:
        return False
    last_string=""
    for the_last in last_word_list:
        last_string += str(the_last)

    return last_string




print(word_upper('gTsdQQalstn'))
print(word_lower('TDadsfaefFSE'))
print(word_lower(12343))
"""
class Calculator():
    def __init__(self):
        pass

    def add(self, x, y):
        add_result = x + y

        return add_result

    def subtract(self, x, y):
        sub_result = x-y
        return float(sub_result)

    def multiply(self, x, y):
        mul_result = int(x*y)
        return int(mul_result)

    def divide(self, x, y):

        div_result = int(x/y)
        div_int = x/y

        if div_int >0:
            float_Value = div_int - div_result


            if float_Value >=0.5:
                div_result+=1
                return int(div_result)
            else :
                return int(div_result)

        else:
            float_Value = div_int - div_result

            if float_Value<=-0.5:
                div_result-=1
                return int(div_result)
            else:
                return int(div_result)



    def expCalc(self,expStr):
        """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 20을 반환한다.
        ex) expCalc('12+3+5-0')는 20을 반환한다.
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
print(calc.divide(-3,2))
print(calc.subtract(3,6.5))