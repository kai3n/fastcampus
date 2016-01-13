'''
sentence = "I am a boy"

def word_count(sentence):
    return len(sentence.split())

print(word_count(sentence))

###############################################
string1 = "I am a boy"
string2 = ["I", "am", "a", "boy"]
string3 = ("I", "am", "a", "boy")
string4 = {"I" : "am", "a" : "boy"}

def search(string, word):
    if type(string) == list or type(string) == str or type(string) == tuple:
        #또는 밑의 줄의 word in string을 위의 if문에 and 처리해도 되지만, 가독성을 위해 분리했다.
        #단,분리를 하는 경우에는 else: return False 처리를 한번 더 해줘야 한다.
        #따라서 짧은 코드를 선호하는 경우에는 if문내에, 명시적이고 가독성이 좋은 코드를 선호하는 경우에는 nested if를 사용하는 것이 좋겠다
        if word in string:
            return True
        else:
            return False
    else:
        return False

print(search(string2, "you"))
'''

###############################################
def range_function(string, start, end, step):
    index = start
    element_list = []
    while index < end:
        element_list.append(string[index])
        index += step
    return element_list

string = "abcdefghijklmnop"
print(range_function(string, 2, 7, 2))

