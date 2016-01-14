"""
word count

def world_count(word):
    word_cnt = word.count(' ') + 1
    return word_cnt

print(world_count('i am a crazy dog 그래 미친개 맞아 미친개'))

def word_count1(word1):
    word_cnt1 = len(word1.split(' '))
    return word_cnt1

print(word_count1('i am a crazy dog. 그래 미친개 맞아 미친개'))

search

def a_search ( target , word ):

    if type(target) == dict:
        return False

    elif type(target) == list:
        target5 = list()
        for i in target:
            target5.append(str(i))
        target_string=','.join(target5)
        a_find= target_string.count(word)
        return bool(a_find)

    else:
        a_find= target.count(word)
        return bool(a_find)

target1 = { 'a': 'b', 'c' : 'd'}
target2 = 'abc'
target3 = ['a','bc','d']
target4 = [1,2,'abc',0.1,'efd']

word1 = 'a'
word2 = 'ab'
word3 = 'd'
word4 = 'e'

print(a_search(target4, word4))

"""

def ran(a,b,c):
    if type(a and b and c) == int:
        e_list = []
        while a < b:
            if c <= 0:
                return "can`t calculating"
            e_list.append(a)
            a = a + c
        else a > b :
             if c >= 0:
                return "can`t calculating"
            e_list.append(a)
            a = a + c
        else:
            return "can`t calculating"
    else:
        return "not range function"

print (ran(20, 28, 4))