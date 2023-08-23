import sys
from collections import deque
si = sys.stdin.readline
n, m = map(int, si().split())

# dfs로 count 계산해서 갈수 있다면 return cnt 아니면 return MAX
maze = [si().strip() for _ in range(n)]
# maze = [[0]*m for _ in range(n)]
# for i in range(n):
#     row = si()
#     for j in range(m):
#         maze[i][j] = int(row[j])
dist = [[0]*m for _ in range(n)]
# dir = [[0,1], [1,0], [0,-1], [-1,0]]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# print(maze)

def bfs():
    queue = deque([0,0])
    # queue = deque()
    # queue.append(0)
    # queue.append(0)
    # print(queue)
    dist[0][0] = 1

    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if dist[nx][ny] != 0: continue
            if maze[nx][ny] == '0': continue
            dist[nx][ny] = dist[x][y] + 1
            # queue.append([nx, ny])
            queue.append(nx)
            queue.append(ny)
            # print(queue)
bfs()
# print(dist)
# for i in dist:
#     print(i)
print(dist[n-1][m-1])