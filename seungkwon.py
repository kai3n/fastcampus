def word_count(word):
    """
    :param word: 넣으려고 하는 문자열
    :return: 그 문자열의 단어 갯수
    """
    return int(len(word.split(" ")))

string_="i love chicken"

print(word_count(string_))