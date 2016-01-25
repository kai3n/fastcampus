import time
from bs4 import BeautifulSoup, Tag
import requests
import urllib


#"http://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1013&weekday=tue"
def download_webtoon(url, path):
    """
    naver webtoon의 이미지를 내가 원하는 폴더에 다운받는다
    :param url: 원하는 웹툰 url
    :param path: 다운받는 절대경로
    """

    html_res =requests.get(url)
    html = BeautifulSoup(html_res.content, "html.parser")

    result = str(html.find_all('img', attrs={"alt":"comic content"})[0]).split(">")
    webtoon = str(result).split(" ")

    img_src = list()
    for idx, src in enumerate(webtoon):
        if src.startswith("src"):
            img_src.append(src[5:-1])

    header = {'Referer':url+'&listPage=1&mobile=y'}

    for source in img_src:
        fileName = str(source).split("/")[-1]
        with open(path+fileName, "wb") as fout:
            response = requests.get(source, stream=True,headers =header)
            # allow_redirects, stream, headers
            fout.write(response.content)


download_webtoon("http://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1013&weekday=tue","/Users/yevgnenll/Desktop/comic/")

#
# url = 'http://imgcomic.naver.net/webtoon/20853/1012/20160114225727_58490cb2cf21c18464d26edbb7203a68_IMAG01_2.jpg'
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19'
req = urllib.Request('http://imgcomic.naver.net/webtoon/20853/1012/20160114225727_58490cb2cf21c18464d26edbb7203a68_IMAG01_2.jpg',
              headers={"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})

html = urllib.urlopen(req).read()


output = open('/Users/yevgnenll/Desktop/comic/tset.jpg','wb')
output.write(html)
output.close()









# find = re.findall("\w+[\w\.]*[\w\-]*@\w+[\w\.]*\.[A-Za-z]+",a)
# second = re.findall("[\w\_\-\.]*@\w*[\w\.]+[\w]+",a)
#
# print(find)
# print(second)




# 테스트를 위한 데코레이션
def elapsed_time(func):
    def elsapse(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("============================================================================")
        print("함수이름:",func.__name__)
        print("걸린시간:",(end - start)*1000,"초")
        # print("걸린시간:",(end - start)/24*60*60 ,"초")
        if len(args) >0:
            print("들어온값:", args)
        if len(kwargs):
            print("들어온 값:", kwargs)
        print("이 함수로 실행할 결과:", result)
        print("리턴타입:", type(result))
        print("============================================================================")
        return result
    return elsapse

class Calculator():
    def __init__(self):
        pass

    @elapsed_time
    def add(self, x, y):
        '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'

        return int(x+y)
    @elapsed_time
    def subtract(self, x, y):

        '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return float(x - y)
    @elapsed_time
    def multiply(self, x, y):
        '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
        return int(x * y)

    @elapsed_time
    def divide(self, x, y):
        '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
        if y == 0:
            return "나누기는 0으로 할 수 없음"

        res = float(x/y) #실수로 바꾼다
        mid = str(res).split(".") # . 을 기준으로 나눈다

        if res < 0 and int(mid[1][0]) >= 5:
            res = int(mid[0]) - 1
        elif int(mid[1][0]) >= 5 : #반올림에 해당하는지 확인
            res = int(mid[0]) + 1

        return int(res)

    @elapsed_time
    def expCalc(self,expStr):
        """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
        ex) expCalc('1+3-5')는 -1을 반환한다.
        ex) expCalc('1+3*5')는 20을 반환한다.
        ex) expCalc('1+3+5-0')는 9을 반환한다.
        ex) expCalc('4+3+5/3')는 4을 반환한다.
        """
        # 문자열이 아닌경우의 예외처리
        if type(expStr) != type("str"):
            return "문자열로 입력하세요"

        # 입력받은 문자열에서 숫자만 저장할 변수
        number = list()
        #숫자가 10의자리 이상일경우 중간 저장할 변수
        target = ""
        #연산자를 저장할 변수
        opp = list()

        for op in expStr:
            #모든 문자를 아스키코드로 변경
            ch = ord(op)
            # 숫자일 경우
            if ch >= 48 and ch <= 57:
                #숫자를 문자열로 바꿔서 저장함
                target += str(chr(ch))
            # 연산자가 올경우
            elif ch == 42 or ch == 43 or ch == 45 or ch ==47:
                #먼저 연산자를 opp에 저장하고
                opp.append(chr(ch))
                #연산자가 왔다는건 숫자 입력이 마무리 되었다는 뜻이므로 숫자를 저장
                number.append(int(target))
                #중간 숫자저장하는 변수 초기화
                target = ""

        #마지막 숫자는 무조건 append
        number.append(int(target))

        # 여기서부터 연산 시작,
        # 연산을 위한 중간 변수 첫번째 숫자를 연산하기위한 변수에 첫번째 숫자를 넣는다

        midRes = number[0]
        # 인덱스 접근을 위한 변수 i
        i = 0

        #연산자 갯수만큼 연산을 해야함.
        while i < len(number)-1:

            # 더하기일 경우
            if opp[i] == "+":
                midRes += number[i+1]
            # 빼기일 경우
            elif opp[i] == "-":
                midRes -= number[i+1]
            # 곱하기인 경우
            elif opp[i] == "*":
                midRes *= number[i+1]
            # 나누기인 경우
            elif opp[i] == "/":
                #나누는 수가 0이면 연산이 불가능함
                if number[i+1] == 0:
                    return "나누기 뒤에 0을 입력하면 안되요~!!"
                midRes /= number[i+1]
            #인덱스를 1 더함.
            i+=1
        #결과값 반환
        return int(midRes)

    @elapsed_time
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

        # 문자열이 아닌경우의 예외처리
        if type(expStr) != type("str"):
            return "문자열로 입력하세요"

        number = list()
        target = ""
        opp = list()

        for op in expStr:
            ch = ord(op)
            if ch >= 48 and ch <= 57:
                target += str(chr(ch))
            elif ch == 42 or ch == 43 or ch == 45 or ch ==47:
                number.append(ch)
                number.append(int(target))
                target = ""

        number.append(int(target))

        midRes = number[0]
        i = 0
        #
        # while i < len(number)-1:
        #
        #     if opp[i] == "+":
        #         midRes += number[i+1]
        #     elif opp[i] == "-":
        #         midRes -= number[i+1]
        #     elif opp[i] == "*":
        #         midRes *= number[i+1]
        #     elif opp[i] == "/":
        #         if number[i+1] == 0:
        #             return "나누기 뒤에 0을 입력하면 안되요~!!"
        #         midRes /= number[i+1]
        #     i+=1
        print(number)
        return int(midRes)

calc = Calculator()
# calc.add(1,2)
# calc.subtract(-3,2)
# calc.divide(-3,2)
#calc.expCalc("12+3-5/2+8")

# calc.expCalc("1-300+5-0")


# def word_count(word):
#     """
#     :param word: 넣으려고 하는 문자열
#     :return: 그 문자열의 단어 갯수
#     """
#     return int(len(word.split(" ")))
#
# @elapsed_time
# def search(text, find):
#     """
#     명훈형님 코드에 힌트를 얻어 다시작성함.
#         1. dict형 자료가 들어오면 반드시 False를 반환
#         2. tuple과 list은 같은 로직으로 처리함
#         3. in을 이용해 검색함
#     :param text: 대상 텍스트
#     :param find: 찾아야 하는 텍스트
#     :return: 있을경우 True, 없을경우 False
#     """
#     result = False
#     if type(text) == dict:
#         # dict데이터가 들어오면 반드시 False를 반환
#         return False
#     elif type(text) == str:
#         if text in find:
#             result = True
#     elif type(text) == list or type(text) == tuple:
#         if str(find) in str(text):
#             result = True
#
#     return result
#
# @elapsed_time
# def myRange(start, stop, step):
#     """
#     start~stop까지 step만큼의 숫자 리스트 반환
#     step 양수인지, 음수인지, 0  인지에 대한 경우로 나눔.
#     예외케이스를 고려했지만 분명히 빼먹은 부분이 있을거라 생각함.
#     :param start: 시작하는 숫자
#     :param stop: 끝나는숫자
#     :param step: n, n+1과의 차이
#     :return: 이 함수로 생성된 list반환, 혹은 에러 메세지
#     """
#     num = start
#     result = list()
#
#     if step > 0:
#         if start > stop:
#             return "step에 +를 넣으면 숫자가 작아질 수 없어 ㅜㅜ"
#         while num < stop:
#             result.append(num)
#             num += step
#     elif step < 0:
#         if start < stop:
#             return "-를 넣으면 절대로 숫자가 올라갈수 없어 ㅜ"
#         else:
#             last = start
#             while last > stop:
#                 result.append(num)
#                 num += step
#                 # 중간변수를 사용한 이유: 음수의 경우 stop값 이전의 가장 작은값을 찾아야 함
#                 last = num
#                 #print("num:", num, "last:", last)
#     else:
#         # step이 0인경우
#         return "step은 0보다 크거나 작아야합니다~"
#     return result
#
# @elapsed_time
# def makeUpper(text):
#     """
#     소문자를 대문자로 바꿔준다
#     :param text: string 타입
#     :return:
#     """
#     result = ""
#     # print(type(text) != str)
#     if type(text) != type("str"):
#         return "문자열만 입력해주세요~"
#     else:
#         for txt in text:
#             ch = ord(txt)
#             if ch >= 97 and ch <=122:
#                 ch -= 32
#             result += chr(ch)
#     return result
#
@elapsed_time
def makeLower(text):
    """
    대문자 -> 소문자
    :param text: String 타입만 받음
    :return: 에러시 에러 메세지, 소문자 데이터 반환
    """
    result = "" #결과값이 저장될 위치
    if type(text) != type("str") :
        return "문자열만 입력해주세요~"
    for txt in text:
        ch = ord(txt)
        if ch >= 65 and ch <=90:
            ch += 32
        result += chr(ch)
    return result
#
# @elapsed_time
# def firstSearch(text, find_word):
#     """
#     전체 텍스트에서 원하는 텍스트를 찾아줌 -> 내가 만든거
#     :param text: 전체 텍스트, 리스트, 튜플
#     :param find_word: 찾는 단어
#     :return: 있으면 True, 없으면 False
#     """
#     res = False
#
#     if type(text) == int or type(text) == float:
#         res = "문자열을 입력하세요"
#     else:
#         if type(text) == str:
#             for t in text:
#                 if t == find_word:
#                     res = True
#         elif type(text) == list or type(text) == tuple:
#             for mid in text:
#                 #print(mid)
#                 print("mid: ", mid, len(mid))
#                 element = str(mid).split(" ")
#                 print("element:", element)
#                 for e in element:
#                     print("e:",e)
#                     for s in e:
#                         print("s", s)
#                         if s == find_word:
#                             res = True
#
#         elif type(text) == dict:
#             res = False
#
#     return res



# string_="apple"
# text1 = "i wanna drink coffee"
# text2 = ['coffee maker', 'cheese', 'eggs']
# text3 = ['maker', 'cheese', 'eggs']
# text4 = ('coffee maker', 'cheese', 'eggs')
# text5 = ('maker', 'cheese', 'eggs')
# text6 = ['reservce my flight ticket','i like gem from tanya', 'cookie' ]
# a = [1, 2, 'abc', 0.1, 'efd']
# search(a, 'ab')
# # print(2, search(text2, 123)) #false
# # print(3, search(text3, "coffee")) #false
# # print(4,search(text4, "coffee")) #True
# # print("a", search(a, "a")) #True
# # print(5, search(text5, "coffee"))
# # print("last", search(text6, "coffee"))
# #
# # print(myRange(1,-10,-1))
# # print(myRange(-1,-10,-1))
#
# makeUpper("AcZefh")
# makeLower("AcZefh")
# print(myRange(0,-10,3))
# #데코레이션을 print()로 사용을 했는데 왜 함수 본연의 기능은 작동하지 않을까?
