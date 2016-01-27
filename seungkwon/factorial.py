def factorial(n):
    if n == 0:
        return 1
    elif n == 1 :
        return 1
    return n * factorial(n-1)

def factor(n):
    u = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2,n+1):
        u *= i
    return u

print(factor(3))


def hanoi(n):
    if n == 1 :
        return 1
    if n == 2:
        return 3
    return hanoi(n-1) + 1 + hanoi(n-1)

def hanoi_path(n, start=1, end=2):
    the = 6-start-end
    res = ""
    if n:
        res = hanoi_path(n-1,start, the)
        res += "%s번 디스크를 %s번 폴대에서 %s폴대로 이동하세요\n" %(n, start, end)
        res += hanoi_path(n-1,the, end)
    return res

print(hanoi_path(4))