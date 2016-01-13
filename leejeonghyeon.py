def word_count(word):
    count_cnt =len(list(word.split()))
    return count_cnt
print(word_count("a b c d"))

def word_search(w01, w02):

    for ww01,ww02 in w01.items():
        if w02 in ww01:
            return True
        return False

print(word_search({'a':'b','c':'d'},'c'))
print(word_search({'a':'b','c':'d'},'u'))
