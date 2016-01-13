def world_count(word):
    word_cnt = word.count(' ') + 1
    return word_cnt

print(world_count('i am a crazy dog 그래 미친개 맞아 미친개'))

def word_count1(word1):
    word_cnt1 = len(word1.split(' '))
    return word_cnt1

print(word_count1('i am a crazy dog. 그래 미친개 맞아 미친개'))





