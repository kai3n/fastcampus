graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = str(queue.pop())
        if vertex not in visited:
            visited.add(vertex)
 #           print(graph[vertex], visited)
            queue.extend(graph[vertex]-visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]-set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path+[next]))


#for i in dfs_paths(graph, 'A', 'F'):
#    print(i)

#print(mca(input))

num = int(input())  # 정점 개수 입력
matrix = [[0 for k in range(num)] for i in range(num)]  # 빈 2차원 배열 선언

for i in range(num):
    line = input().split()
    for j, val in enumerate(line):
        matrix[i][j] = int(val)
#print(matrix)

graph = dict()
for i in range(num): # i = 1, 2, 3,
    l = list()
    for j in range(len(matrix[i])): #j = 1, 2, 3
        if matrix[i][j] is not 0:
            l.append(j)
    graph[str(i)] = set(l)
#print(graph)

for i in graph.keys():
    print(str(i), dfs(graph,str(i)))
    print(i, graph.keys())

# graph = {'1': set(['4']),
#          '2': set(['7']),
#          '3': set(),
#          '4': set(['5', '6']),
#          '5': set(['1']),
#          '6': set(['7']),
#          '7': set(['3'])}

