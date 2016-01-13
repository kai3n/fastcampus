'''
def word_count(word):
    word_cnt=word.split(" ")

    return len(word_cnt)

print (word_count('I am a boy'))
'''
def search(string, word):

    if type(string) == list:
        mon = list(string)
        if word in mon:
            return True
        else:
            return False


    elif type(string) == tuple:
        mon = list(string)
        if word in mon:
            return True
        else :
            return False

    elif type(string) == set:
        mon = list(string)
        if word in mon:
            return True
        else :
            return False

    elif type(string) == str:
        mon = set(string)
        mon_word = set(word)
        if mon_word == mon:
            return True
        else :
            return False


    else :
        return False




print(search([1,2],1))
print(search({1,2},1))
print(search((1,2),1))
print(search('aaa','aa'))
print(search('aaaa','aa'))
