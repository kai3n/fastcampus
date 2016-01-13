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



def a_search ( target , word ):

    if type(target) == dict:
        return False
    else:
        a_find= target.count(word)
        return bool(a_find)

target1 = { 'a': 'b', 'c' : 'd'}
target2 = 'abc'
target3 = ['a','bc','d']

word1 = 'a'
word2 = 'ab'
word3 = 'd'

print(a_search(target3, word3))
"""

def ran(a,b,c):
    if type(a+b+c) == int:
        while a < b:
            e_list = []
            e_list.append(a)
            a = a + c
        else:
            return e_list
    else:
        return "not range function"

print (ran(20, 30, 4))