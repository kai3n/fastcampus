def word_count(word):
    """
    :param word: 넣으려고 하는 문자열
    :return: 그 문자열의 단어 갯수
    """
    return int(len(word.split(" ")))

def search(text_no, find_word):
    """
    전체 텍스트에서 원하는 텍스트를 찾아줌
    :param text: 전체 텍스트, 리스트, 튜플
    :param find_word: 찾는 단어
    :return: 있으면 True, 없으면 False
    """
    text = str(text_no)
    res = False
    if type(text) == str:
        resList = list(text.split())
        for mid in resList:
            if mid == find_word:
                res = True
    elif type(text) == list or type(text) == tuple:
        for mid in text:
            #print(mid)
            ele = mid.split(" ")
            for e in ele:
                if e == find_word:
                    res = True
    elif type(text) == dict:
        res = False

    return res

def myRange(start, stop, step):
    """
    start~stop까지 step만큼의 숫자 리스트 반환
    :param start: 시작하는 숫자
    :param stop: 끝나는숫자
    :param step:
    :return:
    """
    num = start
    result = list()

    if step > 0:
        while num < stop:
            result.append(num)
            num += step
    elif step < 0:
        if start < stop and step < 0:
            return "-를 넣으면 절대로 숫자가 올라갈수 없어 ㅜ"
        else:
            last = start
            while last > stop:
                result.append(num)
                num += step
                last = num
                print("num:", num, "last:", last)
    return result

def makeUpper(text):
    for str in text:
          ch =chr(str)

string_="i love chicken"
text1 = "i wanna drink coffee"
text2 = ['coffee maker', 'cheese', 'eggs'] # true
text3 = ['maker', 'cheese', 'eggs'] # false
text4 = ('coffee maker', 'cheese', 'eggs') #true
text5 = ('maker', 'cheese', 'eggs') #false
text6 = ['reservce my flight ticket','i like gem from tanya', 'cookie' ]

print(search(text1, "coffee"))
print(search(text2, "coffee"))
print(search(text3, "coffee"))
print(search(text4, "coffee"))
print(search(text5, "coffee"))
print("last", search(text6, "coffee"))

print(myRange(1,-10,-1))
print(myRange(-1,-10,-1))