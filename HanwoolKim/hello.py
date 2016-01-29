def firstencoding(str, n):
    number_of_list = int((len(str)/n))
    matrix = [[] for i in range(number_of_list)]

    for i in range(len(str)):
        if(i == 0):
            index = 0
        index = i%number_of_list
        matrix[index].append(str[i])
    return matrix

def toString(matrix):
    result = ''
    for i in range(len(matrix)):
        result += "".join(matrix[i])

    return result

# def caesarBoxCipherEncoding2(message):
#     result = ''
#     mid_result = ''
#     str = ''
#
#     mid_result = firstencoding(message, 2)
#     result = firstencoding(mid_result, 2)
#     str = toString(result)
#

# result = firstencoding("aabcba", 2)
# print(type(result))
# #result = firstencoding(result, 2)
# print(result)
# str = toString(result)
# print(str)


