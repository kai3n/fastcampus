import math

"""
4
x
xxxwbbwww
xxxxxxxxxxxx
xxwbwxbwwwxwxwwwbbwxxwbbwwbxbwwwb
"""

def compact_string(count, *args):
    total_string = ""
    length_string = []

    for index in range(count):
        total_string += args[index]
        length_string.append(len(args[index]))
        total_string += " "

    stack = list()
    new_string = ""
    repeated = 0
    length_compact = []

    print(total_string)
    print(length_string)

    for char in total_string:

        last = len(new_string) - 1

        if last >= 0 and char == new_string[last]:
            repeated += 1

            if repeated >= 8:
                new_string += str(9)
                repeated = 0
        else:
            if repeated >= 1:
                new_string += str(repeated + 1)

            if char == " ":
                stack.append(new_string)
                length_compact.append(len(new_string))
                new_string = ""
            else:
                new_string += char
            repeated = 0

    print(length_compact)

    rate_list = []
    for index in range(len(length_string)):
        result = float(length_compact[index])/float(length_string[index])
        rate_list.append(round(result,3))

    return rate_list



print(compact_string(2, "xxxwbbwww","xxxxxxxxxxxx"))

