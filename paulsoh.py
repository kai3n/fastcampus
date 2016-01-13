# def search(list, word):
#     if type(input) == str:
#         if word in list:
#             return True
#     elif type(list) == tuple or type(list) == list:
#         buff = ""
#         for i in list:
#             buff += str(i)
#         if word in buff:
#             return True
#     return False
#
#
# def word_count(word):
#     return len(word.split())
#

def range_function(a, *args):
    a = int(a)
    result = []
    counter = 0
    if len(args) == False:
        if a > 0:
            while(counter < a):
                result.append(counter)
                counter += 1
            return result
        elif a < 0:
            while(counter > a):
                result.append(counter)
                counter -= 1
            return result
        else:
            return False

    elif len(args) == 1:
        if a < args[0]:
            counter = a
            while(counter < args[0]):
                result.append(counter)
                counter += 1
            return result
        elif a > args[0]:
            counter = a
            while(counter > args[0]):
                result.append(counter)
                counter -= 1
            return result
        else:
            return False

    elif len(args) == 2:
        counter = a
        if a < args[0]:
            while(counter < args[0]):
                if args[1] < 0:
                    return False
                result.append(counter)
                counter += args[1]
            return result
        elif a > args[0]:
            while(counter > args[0]):
                if args[1] > 0:
                    return False
                result.append(counter)
                counter += args[1]
            return result
        else:
            return False
    else:
        return False


print(range_function(5))
print(range_function(-5))
print(range_function(0))

print(range_function(10,7))
print(range_function(11,22))

print(range_function(0,10,2))
print(range_function(0,10,-2))
print(range_function(0, -10, -2))

'''
test_string = 'what is my name my name is paul soh hello world'
query_for_test_string = 'name'

test_list = [1,2,'abc', 0.1, 'efd']
query_for_test_list = 'a'

test_dict = {'a':'b', 'c':'d'}
query_for_test_dict = 'a'

#print(word_count(test_string))


print(search(test_string, query_for_test_string))
print(search(test_list, query_for_test_list))
#print(search(test_dict, query_for_test_dict))


#print(dosearch(string, 'is'))
#print(dosearch(string, 'iadfasdfas'))

'''