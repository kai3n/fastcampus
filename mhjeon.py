'''
sentence = "I am a boy"

def word_count(sentence):
    return len(sentence.split())

print(word_count(sentence))

#####################################################################################################################
string1 = "I am a boy"
string2 = ["I", "am", "a", "boy"]
string3 = ("I", "am", "a", "boy")
string4 = {"I" : "am", "a" : "boy"}
string5 = [1,2,'abc',0.1,'efd']

def search(input, word_or_character):
    if type(input) == str:
        if str(word_or_character) in input:
            return True
    elif type(input) == tuple or type(input) == list:
        empty_string = ""
        for element in input:
            empty_string += str(element)
        if word_or_character in empty_string:
            return True
    return False

print(search(string5, "bc"))

#####################################################################################################################
def range_func(input, start, end, step):
    index = start - 1
    element_list = []

    if start >= 0:
        while index < end:
            element_list.append(input[index])
            index += step
        return element_list

    # Todo: backward range functino yet to be coded
    else:
        index = len(input) + start
        while index < end:
            element_list.append(input[index])
            index += step
        return element_list

input = "123456789"
print(range_func(input, -1, -5, -2))

#####################################################################################################################

#승권: 형님 input의 용도는 무엇인가요??

def print_args(*args):
    print("Positional argument tuple:", args)

print_args("adfasdf","Asdfasdf","asdfasdfasdf")

def print_kwargs(**kwargs):
    print('Keyword arguements:',kwargs)

print_kwargs(wine="merlot", entree='mutton', dessert='macaroon')

#####################################################################################################################

def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)

######################################################################################################################
animal = "fruitbat"

def change_and_print_global():
    #global animal
    animal = "wormbat"
    print("inside chang_and_print_global:", animal)

print(animal)
change_and_print_global()
print(animal)

######################################################################################################################
#
# 14일 목요일: 퀴즈 문제
#
def reverse_word(word):
    if len(word)<=0:
        print ("No word")  ####redundant & 프린트와 return None이 둘 다 반환 -> return "No word"로 두 줄을 한 줄로 줄일 수 있겠다
        return None
    else:
        empty_word = ""
        for char in word[::-1]:
            empty_word += char
        word = empty_word
        return word

print(reverse_word(""))
'''

######################################################################################################################
# 날짜: 2016.1.14
# 과제: upper() & lower() 구현
# 내용: upper()와 lower()는 string class의 method이다. 문자열 객체가 method를 호출하면, 각각 대문자와 소문자로 변환한다.
#      파라미터가 string이 아닌 경우에는 attributeError가 발생한다. 정확한 구현을 위해서는 string class 구현과 try-catch 구문을 사용해야 한다.

def change_to_upper(word):
    #인자로 받는 word가 문자열인 경우에만 함수를 실행한다.
    if type(word) != str:
        return "올바른 입력값이 아닙니다."
    #올바른 형태의 인자가 들어왔을 경우만 변환 진행한다.
    else:
        uppered_word = ""
        for i in range(len(word)):
            #소문자가 아닌 경우는 loop에서 다음으로 넘어간다. If구문과 else구문의 순서는 유의미하다.
            #소문자는 ASCII 코드상 97-122에, 대문자는 65-90에 해당한다. 같은 글자의 소문자 - 대문자의 차이는 32이다.
            #함수 ord()는 글자를 해당 ASCII코드 숫자로, chr()는 ASCII 코드를 글자로 변환한다.
            if ord(word[i]) < 97 and ord(word[i]) > 122:
                uppered_word += word[i]
                continue
            #소문자인 경우에만 order()를 통해 숫자로 변환 진행한다.
            else:
                ASCII_char = ord(word[i]) - 32
                uppered_word += chr(ASCII_char)
        return uppered_word

#Change_to_upper()의 코드를 살짝 바꾸면 된다
def change_to_lower(word):
    if type(word) != str:
        return "올바른 입력값이 아닙니다."
    else:
        lowered_word = ""
        for i in range(len(word)):
            #대문자가 아니면 다음 글자로 넘어간다.
            if ord(word[i]) < 65 or ord(word[i]) > 90:
                lowered_word += word[i]
                continue
            else:
                ASCII_char = ord(word[i]) + 32
                lowered_word += chr(ASCII_char)
        return lowered_word

test_string1 = "abBzrTsdf134"
test_string2 = 1234

print(change_to_upper(test_string1))
print(change_to_upper(test_string2))
print(change_to_lower(test_string1))
print(change_to_lower(test_string2))

######################################################################################################################
'''
def countdown(n):
    print('counting down from %d' %n)
    while n > 0:
        yield n
        n -= 1
    return

print(type(countdown))
'''
