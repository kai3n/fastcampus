def dfs(n, matrix, start):
    adj = matrix
    visited = [0 for i in range(n)]
    st = [start]

    while(st):
        vertex = st.pop()
        visited[i] = 1

        for i in range(len(adj[vertex])):
            if (visited[i] == 0 and adj[vertex][i] == 1):
                st.append(i)
    return visited

def dfsAll(n):
    result = []

    for i in range(n):
        print((dfs(n, matrix, i)))

n = 7
matrix = [[0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0],
          [1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 1, 0, 0, 0, 0]]

print(dfsAll(n))