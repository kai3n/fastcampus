test_list = [1,2,'abc', 0.1, 'efd']
query_for_test_list = 'a'



def search(sentance, word):
    if type(sentance) == str and type(word) == str:
        if word in sentance:
            return True
    elif type(sentance) == tuple or type(sentance) == list:
        for i in range(0,len(sentance)):
            if type(sentance[i]) == int or type(sentance[i]) == float:
                if sentance[i] == word:
                    return True
            elif word in sentance[i]:
                return True
    return False

print(search(test_list, query_for_test_list))


def word_count(word):
    return len(word.split())


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


test_string = 'what is my name my name is paul soh hello world'
query_for_test_string = 'name'



test_dict = {'a':'b', 'c':'d'}
query_for_test_dict = 'a'

#print(word_count(test_string))
print(search(test_string, query_for_test_string))
print(search(test_dict, query_for_test_dict))


#print(dosearch(string, 'is'))
#print(dosearch(string, 'iadfasdfas'))

