"""
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

    word = word.lower()

    for val in new_list:
        val = val.lower()
        if val == word:
            return True
    return False

#print(search({'a':'b'}, "COPY"))
print(search("Return a copy of the string", "return"))
"""


# 3. range 함수 구현
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
        if start_num < end :
            number_list.append(start_num)
        else:
            break
    return number_list


print(make_range(1,10,-1))


