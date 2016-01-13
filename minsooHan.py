'''
def word_count(word):
    word_cnt=word.split(" ")

    return len(word_cnt)

print (word_count('I am a boy'))
'''
def search(string, word):
    list_check=[1,2]
    tuple_check=(1,2)
    set_check={1,2}
    string_check='check'

    if type(string) == type(list_check):
        mon = list(string)
        if word in mon:
            return True
        else:
            return False


    elif type(string) == type(tuple_check):
        mon = list(string)
        if word in mon:
            return True
        else :
            return False

    elif type(string) == type(set_check):
        mon = list(string)
        if word in mon:
            return True
        else :
            return False

    elif type(string) == type(string_check):
        mon = set(string)
        mon_word = set(word)
        if mon_word == mon:
            return True
        else :
            return False


    else :
        return False




print(search((1,2),1))
print(search('aaa','aa'))
