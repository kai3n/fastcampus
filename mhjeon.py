sentence = "I am a boy"

def word_count(sentence):
    return len(sentence.split())

print(word_count(sentence))

#####################################################################################################################
string1 = "I am a boy"
string2 = ["I", "am", "a", "boy"]
string3 = ("I", "am", "a", "boy")
string4 = {"I" : "am", "a" : "boy"}
string5 = [1,2,'abc',0.1,'efd']

def search(input, word_or_character):
    if type(input) == str:
        if word_or_character in input:
            return True
        else:
            return False
    elif type(input) == tuple or type(input) == list:
        empty_string = ""
        for element in input:
            empty_string += str(element)
        if word_or_character in list(empty_string):
            return True
        else:
            return False
    return False

print(search(string5, "b"))

#####################################################################################################################
def range_func(input, start, end, step):
    index = start - 1
    element_list = []
    while index < end:
        element_list.append(input[index])
        index += step
    return element_list

input = "012345678"
print(range_func(input, 2, 7, 2))

#####################################################################################################################

