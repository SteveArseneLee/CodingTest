import sys
# from collections import deque
si = sys.stdin.readline

r, c = map(int, si().split())
alphas = [si().strip() for _ in range(r)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = 0
def bfs(x,y):
    global result
    q = set()
    q.add((x,y,alphas[x][y]))
    # print(q)
    while q:
        # print(q)
        x,y,step = q.pop()

        result = max(result, len(step))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동할 수 있는 위치면서 새로운 알파벳인 경우
            if (0<=nx and nx<r and 0<=ny and ny < c and alphas[nx][ny] not in step):
                q.add((nx, ny, step + alphas[nx][ny]))

bfs(0,0)
print(result)