'''
what = 'I love you'

def word_counts(what):
    how = len(what.split())
    return how

print(word_counts(what))


def search(string,word):

    if type(string) == tuple:

        if word in string:
            return True

    elif type(string) == list:

        new = tuple(string)

        if word in new:
            return True

    elif type(string) == str:
        if word in string:
            return True
    else:
        pass

    return False

print(search('abc','a'))


class Calculator():
     def __init__(self):
         pass
     def add(self, x, y):
         '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
         return int(x+y)
     def subtract(self, x, y):
         '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'

         return float(x+y)
     def multiply(self, x, y):
         '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
         return int(x*y)

     def divide(self, x, y):
         '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'

         experiment = float(x/y) - int(x/y)
         second_experiment = int(experiment*10)

         if second_experiment > 4:
             third_experiment = int(x/y)+1

             return third_experiment

         elif -5 < second_experiment < 5:
             third_experiment = int(x/y)

             return third_experiment

         else:

             third_experiment = int(x/y)-1

             return third_experiment

     def expCalc(self,expStr):
         """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
         ex) expCalc('1+3-5')는 -1을 반환한다.
         ex) expCalc('1+3*5')는 20을 반환한다.
         ex) expCalc('1+3+5-0')는 9을 반환한다.
         ex) expCalc('4+3+5/3')는 4을 반환한다.
"""
         number = []
         operation =  []

         for first_validation in expStr:

             if type(first_validation) == int:

                 number =+ first_validation








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
print(calc.multiply(3,2))
print(calc.divide(7,-3))
'''


def upper(string):

    if type(string) == str:

        character_list = []

        for using_character in string:

            converting_character = ord(using_character)

            if 96< converting_character <123:

                converted_character = converting_character - 32

                character = chr(converted_character)

                character_list.append(character)

            else:

                character = chr(converting_character)
                character_list.append(character)


        return "".join(character_list)

    else:
        print("Wrong!")

def lower(string):

    if type(string) == str:

        character_list = []

        for using_character in string:

            converting_character = ord(using_character)

            if 64< converting_character <97:

                converted_character = converting_character + 32

                character = chr(converted_character)

                character_list.append(character)

            else:

                character = chr(converting_character)
                character_list.append(character)


        return "".join(character_list)

    else:
        print("Wrong!")

print(upper("abcd"))
print(upper("aBcd"))
print(upper("aB1d"))
print(upper(1))
print(upper("1"))

print(lower('ABCD'))
print(lower('aBcd'))
print(lower('1Be!'))
print(lower(1))