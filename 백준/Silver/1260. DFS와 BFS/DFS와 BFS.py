from collections import deque

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for e in adj[start]:
        if not visited[e]:
            dfs(e)

# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if not visited[v]:
#             visited[v] = True
#             print(v, end=' ')
#             for e in adj[v]:
#                 if not visited[e]:
#                     q.append(e)

def bfs(start):
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in adj[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            

# n : 정점의 개수, m : 간선의 개수, v : 탐색을 시작할 정점의 번호
n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    
for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)