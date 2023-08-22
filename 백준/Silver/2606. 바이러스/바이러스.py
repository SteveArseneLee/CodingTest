def dfs(pos):
    global count
    count += 1
    visited[pos] = True
    for next_pos in adj[pos]:
        if not visited[next_pos]:
            dfs(next_pos)
            
n, m = int(input()), int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    x,y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    
dfs(1)
print(count-1)