def search(list, word):
    try:
        return bool(list.count(word))
    except:
        print("Input not valid, try again")
        return False


def word_count(word):
    return len(word.split())


def range(a,b):



test_string = 'what is my name my name is paul soh hello world'
query_for_test_string = 'name'

test_list = ['a', 'ab', 'ac', 'add']
query_for_test_list = 'ac'

test_dict = {'a':'b', 'c':'d'}
query_for_test_dict = 'a'

#print(word_count(test_string))


print(search(test_string, query_for_test_string))
print(search(test_list, query_for_test_list))
print(search(test_dict, query_for_test_dict))


#print(dosearch(string, 'is'))
#print(dosearch(string, 'iadfasdfas'))

