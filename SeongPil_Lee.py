import time


def elapsed_time(functor):
	def decorated(*args,**kwargs):
		start = time.time()
		functor(*args,**kwargs)
		end = time.time()
		print("elapsed time:%f" %(end - start))
	return decorated

@elapsed_time
def hello():
     for i in range(1000):
         for j in range(100):
             pass
hello()

@elapsed_time
def wd_count(wd):
    wd_cnt = 0
    wds = str(wd)
    wd_cnt = len(wds.split(' '))
    return wd_cnt

print(wd_count('asdf sdf'))


@elapsed_time
def word_count(word):
    word_cnt = 0
    words = str(word)
    word_cnt = len(words.split(' '))
    return word_cnt

print(word_count('sadf'))
#
# print(word_count('ssd sd s sd sd sd '))
# @elapsed_time
# def search(string, word):
#     if type(string) == str:
#         if word in string:
#             return True
#         else:
#             return False
#     elif type(string) == list or type(string) == tuple:
#         if type(word) == str:
#             strings = []
#             for item in string:
#                 if type(item) == str:
#                     strings.append(item)
#                 else:
#                     continue
#             for checkStr in strings:
#                 if word in checkStr:
#                     return True
#                 else:
#                     continue
#             return False
#
#         elif type(word) == int:
#             integers = []
#             for item in string:
#                 if type(item) == int:
#                     integers.append(item)
#                 else:
#                     continue
#             for checkInt in integers:
#                 if word in integers:
#                     return True
#                 else:
#                     continue
#             return False
#
#         elif type(word) == float:
#             floats = []
#             for item in string:
#                 if type(item) == float:
#                     floats.append(item)
#                 else:
#                     continue
#             for checkFloat in floats:
#                 if word == checkFloat:
#                     return True
#                 else:
#                     continue
#             return False
#
#     else:
#         return 'Type Error'
#
# print(search(['apple', 1, 0.1, 8, 0.4,'power'], 0.4))
#
# def num_range(start, end, step):
#     num_list = []
#     if step == 0:
#         return 'error: step must not be Zero'
#     elif step > 0:
#         if start < end:
#             while start < end:
#                 num_list.append(start)
#                 start += step
#             return num_list
#         else:
#             return []
#     elif step < 0:
#         if start > end:
#             while start > end:
#                 num_list.append(start)
#                 start += step
#             return num_list
#         else:
#             return []
#     else:
#         return 'Unknown Error'
#
# print(num_range(22, 22, 1))
#
#
# def new_upper(string):
#     if type(string) == str:
#         pass
#     else:
#         return None
#     chars = ''
#     for char in string:
#         asci = ord(char)
#         if 96 < asci and asci < 123:
#             asci -= 32
#             chars += chr(asci)
#         elif 64 < asci and asci < 91 or asci == 32:
#             chars += chr(asci)
#         else:
#             return 'arg must be only str'
#     return chars
#
# print(new_upper('PlAnRi abLUeu'))
#
# def new_lower(string):
#     chars = ''
#     for char in string:
#         asci = ord(char)
#         if 64 < asci and asci < 91:
#             asci += 32
#             chars += chr(asci)
#         elif 96 < asci and asci < 123 or asci == 32:
#             chars += chr(asci)
#         else:
#             return 'arg must be only str'
#     return chars
#
# print(new_lower('SuPeR PoWeR'))
