def search(list, word):
    try:
        return bool(list.count(word))
    except:
        print("Input not valid, try again")
        return False


def word_count(word):
    return len(word.split())


def range_function(a, *args):
    result = []
    if len(args) == False:
        print(range(0,a))
        return range(0,a)
    elif len(args) == 1:
        print(range(a, args[0]))
        return range(a,args[0])
    elif len(args) == 2:
        print(range(a, args[0], args[1]))
        return range(a, args[0], args[1])



range_function(5)
range_function(0,7)
range_function(0,10,2)


'''
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

'''