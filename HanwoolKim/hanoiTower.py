def hanoiTower(n):

    if (n == 1):
        return 1

    else:
        return hanoiTower(n-1)*2 + 1

print(hanoiTower(10))


# def hanoi(n,start,end,mid):
#
#     if(n == 1):
#         print("%d번 디스크를 %d에서 %d로 옮기시오" %(n,start,end))
#
#     else:
#         hanoi(n-1, start, mid, end)
#         hanoi(1, start, end, mid)
#         hanoi(n-1, mid , end, start)
#
# print(hanoi(2,1,3,2))

def hanoi(n,start,end,mid):

 if n:
        hanoi(n-1, start, mid, end)
        print("%d 디스크를 %d에서 %d로 옮기시오" %(n, start, end))
        hanoi(n-1, mid , end, start)

print(hanoi(3,1,3,2))
