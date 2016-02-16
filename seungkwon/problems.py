def rentangle(n):
    res = [None]*(n**2)
    height = n
    below = 3*n-2
    up = 3*n-1
    # print(res, len(res))
    for num in range(1, n*n+1):
        if num <= n-1: #first
            res[num-1] = num
        elif num % n == 0: # height
            res[num-1] = height
            height += 1
        # elif num % n == 1: # up
        #     res[num-1] = up
        #     up += 1
        elif n**2-n+1 <= num and num < n**2: # below
            res[num-1] = below
            below -= 1
        # else:
        #     res[num-1] = 0
    return res

def start(n):
    for i in range(1,n+1):
        print(" "*(n-i), end='')
        print("*"*i)

# print(start(6))
a = dict()

def arrayMaxConsecutiveSum(inputArray, k):
    ans = 0
    for i in range(len(inputArray)-k+1):
        ans = max(sum(inputArray[i:i+k]), ans)
    return ans

def myMaxOfThree(a,b,c):
    mid = 0
    if a< b:
        mid = b
        if mid > c:
            return mid
        else:
            return c
    else:
        mid = a
        if mid < c:
            return c
        else :
            return mid

def com(n,k ):
    def facto(a):
        if a >= 1:
            a *= (a-1)
        return facto(a)

    return facto(k)/(facto(n)*facto(k-n))

def coutpira(n):
    for a in range(1,n+1):
        print()


def mca(s):
    """
    xxxxaaab -> x4a3b
    단 최대 압축은9 이후는 9,x9x3 이런 방식으로 압축한다
    :param s:
    :return:
    """
    mid =s[0]
    cut = list()
    result = ""
    i = 1
    for st in s[1:]:
        # print("st:", st, "mid-length:", len(mid),"mid:", mid)
        if st == mid[0]:
            # 같은 문자열이 올 경우
            mid += st
        else :
            # 다른 문자열이 올 경우
            if mid[0] != st:
                # 새로운 문잘열이 옴
                cut.append(mid) # xxxx를 붙인다
                mid = st
            elif len(mid) < 2:
                cut.append(st)
        i+=1
    if i == len(s):
        cut.append(mid)
    #
    # for c in cut:
    #     print(c, len(c))
    # 같은 문자열들을 더한다
    for same in cut:
        # 같은 문자열의 갯수가 9개 이하
        if len(same) > 1 and len(same)<= 9:
            result +=str(same[0])+str(len(same))
        # 같은 문자열의 갯수가 9 이상
        elif len(same) > 9:
            nine = len(same)/9
            mod = len(same)%9
            for a in range(int(nine)):
                result += same[0] +"9"
            if mod > 1:
                result += same[0] + str(mod)
            else:
                result+=same[0]
        else:
            result += same
    # print(result)
    return round(float(len(result)/len(s)),3)

# print("xxxwbbwww",mca("xxxwbbwww"))
# print(mca("hhhhhhllllllllllbbbbbbbbnnnnnnnnnnnnnooooooooooooooorrrbbbbbbbbbbbbbbyyyyqqqqqqqqqqqqqqvvvvwwwwwwwwwwbwwwnnnnn"))

# print(mca("lllllllllllllwwwwwwwwwvvvvvvvvgsssnnnoooooooooooowwwwwwwwwwwwwqqqqqqqqqqqggggggggggggggggtttttttkkkkkkkkkkkk"))
# print(mca("a"))
# print(mca("gkkkk ttttt ttttt tt bbbb lllll lllll lll ppppp ppppp ppppp ggggg g ddd i yyyyyy ggggg ggggg ddddd xxxxx xxxxx xxxxx x ff"),0.357)
print(mca("gkkkkttttttttttttbbbblllllllllllllpppppppppppppppggggggdddiyyyyyyggggggggggdddddxxxxxxxxxxxxxxxxff"), 0.357)
# print(mca(""))
# print(mca(""))
# print(mca(""))
# print(mca(""))
# print(mca(""))
# print(mca(""))

# gk4t9t3b4l9l4p9p6g6d3iy6g9g1d5x9x7f2
# gk4t9t3b4l9l4p9p6g6d3iy6g9gd5x9x7f2





