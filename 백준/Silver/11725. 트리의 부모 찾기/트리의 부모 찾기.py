import sys
si = sys.stdin.readline

n = int(si())
adj = [[] for _ in range(n+1)]
parent = [0] * (n+1)
sys.setrecursionlimit(100000)
for _ in range(n-1):
    x, y = list(map(int, si().split()))
    adj[x].append(y)
    adj[y].append(x)

# print(adj)
def dfs(x, par):
    # print(par)
    # print("parent : ", parent)
    for y in adj[x]:
        if y == par:
            # print("same case", y)
            continue
        parent[y] = x
        dfs(y, x)

# dfs(1,-1)
# print(parent)
# for i in range(2, n+1):
#     print(parent[i])
# print()
# parent = [0] * (n+1)
dfs(1,0)
# print(parent)
for i in range(2, n+1):
    print(parent[i])