def word_count(word):
    word_cnt = 0
    words = str(word)
    word_cnt = len(words.split(' '))
    return word_cnt

print(word_count('어려서부터 우리집은 가난했었고, 남들 가는 외식 한번 간적 없었고'))

# def search(string, word):
    # if type(string) == dict:
    #     return False
    # elif type(string) == str:
    #     if word in string:
    #         return True
    #     else:
    #         return False
    # elif type(string) == list:
    #     if type(word) == str:
    #         for item in string:
    #             if word in item:
    #                 return True
    #     else:
    #         if word in string:
    #             return True
    #         else:
    #             return False
    #     if word in string:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False

    # if type(string) == str:
    #     if word in string:
    #         return True
    #     else:
    #         return False
    # elif type(string) == tuple or type(string) == list:

# print(search(['apple', 1, 0.1], '1'))

def num_range(start, end, step):
    num_list = []
    if step == 0:
        return print('error: step must not be Zero')

    if start < end:
        if step > 0:
            while start < end:
                num_list.append(start)
                start += step
            return num_list
        elif step < 0:
            return []
        else:
            print('error: I don\'t know what happened')
    elif start > end:
        if step < 0:
            while start > end:
                num_list.append(start)
                start += step
            return num_list
        elif step > 0:
            return []
        else:
            print('error: I don\'t know what happened')
    else:
        return []

print(num_range(10,10,0))


