
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
print(word_lower(123))

