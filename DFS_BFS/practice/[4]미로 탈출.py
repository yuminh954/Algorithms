from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 1
queue = deque()
queue.append((0,0))

def bfs(graph, i, j) :
    while queue :
        i, j = queue.popleft()
        for k in range(4) :
            next_x = i + dx[k]
            next_y = j + dy[k]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m :
                continue
            if graph[next_x][next_y] == 0 :
                continue
            if graph[next_x][next_y] == 1 :
                queue.append((next_x,next_y))
                graph[next_x][next_y] = graph[i][j] + 1

    return graph[n-1][m-1]

cnt = bfs(graph, 0, 0)
print(cnt)