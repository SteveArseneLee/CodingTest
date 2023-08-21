import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def dfs(x):
    # x의 인접노드들 확인
    for data in graph[x]:
        y = data[0]
        cost = data[1]
        if not visited[y]:
            visited[y] = True
            distance[y] = distance[x] + cost
            dfs(y)

n, m = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))
# print(graph)

# m개만큼 거리를 알려줭
for _ in range(m):
    x,y = map(int, input().split())
    # 방문 여부 및 최단 거리 테이블
    visited = [False] * (n+1)
    distance = [-1] * (n+1)
    visited[x] = True # 시작점 방문 처리
    distance[x] = 0 # 자신까지 거리 0
    dfs(x)
    print(distance[y])