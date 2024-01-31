# 한번 들어갔다 나오면 cnt += 1
# 한번 들어갔을 때는 상하좌우 각 방향으로 재귀적으로 호출한다.
n, m = map(int, input().split())
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, i, j) :
    # 방문 처리
    if graph[i][j] == 0 :
        graph[i][j] = 1
        # 상/하/좌/우 돌면서 들어가기
        for k in range(4) :
            if i + dx[k] < 0 or i + dx[k] >= n or j + dy[k] < 0 or j + dy[k] >= m :
                continue
            dfs(graph, i + dx[k], j + dy[k])
        return True
    else :
        return False
        
cnt = 0

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            if dfs(graph, i, j) == True :
                cnt += 1

print(cnt)