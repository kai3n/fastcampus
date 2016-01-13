def word_count(word):
    word_cnt=word.split(" ")

    return len(word_cnt)

print (word_count('I am a boy'))

def search(string, word):
    match = 0
    list_check=[1,2]
    tuple_check=(1,2)
    set_check={1,2}

    if type(string) == type(list_check):
        return True

    elif type(string) == type(tuple_check):
        return True

    elif type(string) == type(set_check):
        return True

    else :
        return False




print(search([1,2],'s'))
