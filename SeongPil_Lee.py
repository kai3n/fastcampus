def word_count(word):
    word_cnt = 0
    words = str(word)
    word_cnt = len(words.split(' '))
    return word_cnt

print(word_count('어려서부터 우리집은 가난했었고, 남들 가는 외식 한번 간적 없었고'))

def search(string, word):
    if type(string) == dict:
        return False
    elif type(string) == str:
        if word in string:
            return True
        else:
            return False
    elif type(string) == list:
        if word in string:
            return True
        else:
            return False
    else:
        return False

print(search({'a':'a', 'b':'b'}, 'a'))

def num_range(start, end, step):
    num_list = []
    while start < end:
        num_list.append(start)
        start += step
    return num_list

print(num_range(0,10,2))
