'''
def word_count(word):
    word_cnt=word.split(" ")

    return len(word_cnt)

print (word_count('I am a boy'))
'''
def search(string, word):


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
