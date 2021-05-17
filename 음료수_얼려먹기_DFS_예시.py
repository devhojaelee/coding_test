# dfs에서는 가장 깊은 원소까지 들어간다.
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)  # 상하좌우는 리턴값을 사용하지 않아서
        dfs(x, y-1)  # 그냥 방문한 노드만 체크
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


n, m = map(int, input().split())
graph = []  # 이차원 배열 정의 헷갈렸어.

for i in range(n):
    graph.append(list(map(int, input())))

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
