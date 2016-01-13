"""
# 1. 문장이 들어오면 해당 문장을 단어별로 끊어, 단어 갯수 리턴
def word_count(word):
    words_list = word.split(" ")
    word_cnt = len(words_list)
    return word_cnt

print(word_count("Return a copy of the string where all tab characters are"\
                +"replaced by one or more spaces, depending on the current column"\
                +"and the given tab size. Tab positions occur every tabsize characters"))
"""

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
