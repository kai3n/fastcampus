sentence = "I am a boy"

def word_count(sentence):
    return len(sentence.split())

print(word_count(sentence))

def search(string, word):
    if type(string) == list or str or tuple:
        #string인자를 list로 타입 캐스트한다. 리스트, 문자열, 튜플은 모두 리스트 가능하다.
        if word in list(string):
            return True
    else:
        return False