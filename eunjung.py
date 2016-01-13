def word_count(word):
    words_list = word.split(" ")
    word_cnt = len(words_list)
    return word_cnt

print(word_count("Return a copy of the string where all tab characters are"\
                +"replaced by one or more spaces, depending on the current column"\
                +"and the given tab size. Tab positions occur every tabsize characters"))