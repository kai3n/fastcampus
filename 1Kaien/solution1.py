#input = "xxwbwxbwwwxwxwwwbbwxxwbbwwbxbwwwb"

def mca(input):
    output = ""
    begin = 0
    end = 1

    for i in range(len(input)):
        output += input[begin]
        if begin == len(input)-1:
            break
        while input[begin] == input[end]:
            if end - begin == 9:
                break
            end += 1
        if end - begin > 1:
            output += str(end-begin)
        begin = end
        end += 1
    return output

#print(mca(input))

num = int(input())  # 정점 개수 입력
matrix = [[0 for k in range(num)] for i in range(num)]  # 빈 2차원 배열 선언

for i in range(num):
    line = input().split()
    for j, val in enumerate(line):
        matrix[i][j] = int(val)
print(matrix)

