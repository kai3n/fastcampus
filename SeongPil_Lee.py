def word_count(word):
    word_cnt = 0
    words = str(word)
    word_cnt = len(words.split(' '))
    return word_cnt

print(word_count('어려서부터 우리집은 가난했었고, 남들 가는 외식 한번 간적 없었고'))