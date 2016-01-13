def do_nothing():
    pass

def make_a_sound():
    print('quack')

def agree(num):
    return "apple" + " " + str(num)

def search(word):
    some_list = ["apple","cat","dragon","egg"]
    for val in some_list:
        if val == word:
            print("있음")
        else:
            print("없음")
        break


# do_nothing()
# make_a_sound()
# a = agree(10)
# print(type(a))

search('bee')