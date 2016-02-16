from HanwoolKim import linked_binarytree

def calculator(s):

    char_list = []
    prior = []
    depth = 0
    max_depth = 0
    something = []

    for char in s:
        if(char == '('):
            depth += 1
            max_depth = max(max_depth,depth)
            continue
        elif(char == ')'):
            depth -= 1
            continue
        prior.append(depth)
        char_list.append(char)

    print(prior)
    print(char_list)
    print(max_depth)
    for j in range(max_depth,0,-1):
        for i in range(0,len(prior)):
            if(prior[i] == j):
                print("what is i" ,i)
                something = change(char_list,i+1)
                print (something)



def change(lst, index):
    result = []
    result += lst[0:index]
    result += lst[index+1:]
    result.append(lst[index])
    return result

calculator("(3+1)*(2+(4*8))")





