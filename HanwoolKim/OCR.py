
def find(n):
    result = []
    for char in n:
        list = ['h', 'e']
        #print(char)
        if char in list:
            result.append(char)

    return result

n = "heooooooooolllooohhhhhllooollololo"

# result = []
# for c in find(n):
#     result.append(c)

print(find(n))