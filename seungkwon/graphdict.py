graph = {
    'A': set(['B','C']),
    'B': set(['A','D','E']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}
# print(graph)

def dfsTeach(graph, start):
    """
    경로를 돌면서 출력하는 함수,
    :param graph: 그래프
    :param start: 해당 그래프에서 시작점
    :return: depth가 나온다(모두 방문한 결과)
    동그라미 체크가 add한 것임.
    """
    visited, stack = set(), [start]
    while stack:
        vertax = stack.pop()
        if vertax not in visited:
            visited.add(vertax)
            stack.extend(graph[vertax] - visited)

    return visited



def dfs(graph, start):
    """
    경로를 돌면서 출력하는 함수,
    :param graph: 그래프
    :param start: 해당 그래프에서 시작점
    :return: depth가 나온다(모두 방문한 결과)
    동그라미 체크가 add한 것임.
    """
    # visited -> 방문한 곳
    # stack -> 경로를 체크해야 하는곳
    visited, stack = set(), [start]
    while stack:
        vertax = stack.pop()
        if vertax not in visited:
            stack.extend(graph[vertax] - visited)
            if vertax == start:
                if len(visited) > 0:
                    visited.add(vertax)
            else:
                visited.add(vertax)



    return visited

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertax, path) = stack.pop()
        for next in graph[vertax] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [ next]))

for i in dfs_path(graph, "A", "A"):
    print("m", i)

# print(dfs_path(graph,"A", "B"))

# print(dfs(graph, 'A'))

ar = [ [0,0,0,1,0,0,0],
      [0,0,0,0,0,0,1],
      [0,0,0,0,0,0,0],
      [0,0,0,0,1,1,0],
      [1,0,0,0,0,0,0],
      [0,0,0,0,0,0,1],
      [0,0,1,0,0,0,0]
      ]





def findPath(n):
    #
    # arr = list()
    # for c in range(n):
    #     arr.append(input("입력하셈: "))
    # print(arr)
    graph = dict()
    mid = list()
    for a, li in enumerate(n):
        # 각각 줄에서
        for idx, i in enumerate(li):
            # 방향 1이면 갈 수 있음
            if i == 1:
                mid.append(idx)

        graph[a] = set(mid)
        mid = list()
    # print(graph)
    result= dict()
    for id in range(len(graph)):
        result[id]= dfs(graph, id)

    print(result)
    miRes = [[0 for k in range(len(n))] for i in range(len(n))]  # 빈 2차원 배열 선언
    print(miRes)
    for i in range(len(result)):
        resultCol = list(result[i])
        for j in resultCol:
            miRes[i][j] = 1
    return miRes

# print(findPath(ar))

# for a in findPath(ar):
#     print(a, findPath(ar)[a])
# a = [["a"]*5]*5
# print(a)

def chageDictGraph(n):
    graph = dict()
    mid = list()
    for a, li in enumerate(n):
        # 각각 줄에서
        for idx, i in enumerate(li):
            # 방향 1이면 갈 수 있음
            if i == 1:
                mid.append(idx)

        graph[a] = set(mid)
        mid = list()
    # print(graph)
    result= dict()
    for id in range(len(graph)):
        result[id]= dfs(graph, id)
    return result

print("result:", findPath(ar))


print(0,dfs(chageDictGraph(ar), 0))
print(1,dfs(chageDictGraph(ar), 1))
print(2, dfs(chageDictGraph(ar), 2))
print(3, dfs(chageDictGraph(ar), 3))
print(4,dfs(chageDictGraph(ar), 4))
print(5,dfs(chageDictGraph(ar), 5))
print(6,dfs(chageDictGraph(ar), 6))