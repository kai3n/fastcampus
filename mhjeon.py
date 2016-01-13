sentence = "I am a boy"

def word_count(sentence):
    return len(sentence.split())

print(word_count(sentence))

#####################################################################################################################
string1 = "I am a boy"
string2 = ["I", "am", "a", "boy"]
string3 = ("I", "am", "a", "boy")
string4 = {"I" : "am", "a" : "boy"}

def search(string, word_or_character):
    if type(string) == str:
        if word_or_character in string:
            return True
        else:
            return False
    elif type(string) == tuple or type(string) == list:
        empty_string = ""
        for word in string:
            empty_string += word
        if word_or_character in list(empty_string):
            return True
        else:
            return False
    return False

print(search(string2, "o"))

#####################################################################################################################
def range_func(string, start, end, step):
    index = start - 1
    element_list = []
    while index < end:
        element_list.append(string[index])
        index += step
    return element_list

string = "012345678"
print(range_func(string, 2, 7, 2))

#####################################################################################################################

