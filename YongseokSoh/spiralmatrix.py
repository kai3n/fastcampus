n = 10


sm = []
for i in range(n):
    sm.append([])
    for j in range(n):
        sm[i].append(0)

x = 0
y = 0
dir = 1 # 1 is left, 2 is down, 3 is right, 4 is up, 1 is left

for i in range(1,n*n+1):
    sm[x][y] = i
    if dir is 1: # x, y+1
        if y+1>=n or sm[x][y+1] is not 0:
            dir += 1
            x = x+1
        else:
            y = y+1
            sm[x][y] = i
    elif dir is 2: # x+1. y
        if x+1>=n or sm[x+1][y] is not 0:
            dir += 1
            y = y-1
        else:
            x = x+1
            sm[x][y] = i
    elif dir is 3: # x. y-1
        if y-1<0 or sm[x][y-1] is not 0:
            dir += 1
            x = x-1
        else:
            y = y-1
            sm[x][y] = i
    elif dir is 4: # x-1, y
        if x-1<0 or sm[x-1][y] is not 0:
            dir = 1
            y = y+1
        else:
            x = x-1
            sm[x][y] = i

for line in sm:
    print(line)