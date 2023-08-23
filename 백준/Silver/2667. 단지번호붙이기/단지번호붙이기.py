import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    result = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<=-1 or nx>=n or ny<=-1 or ny>=n:
            continue
        # 처음 방문할 때
        if arr[nx][ny] == 1:
            arr[nx][ny] = -1
            result += dfs(nx,ny)
    return result


# 지도 크기
n = int(input())
# arr = [list(input()) for _ in range(N)]
arr = [[0]*n for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(n):
        arr[i][j] = int(row[j])
# print(arr)
answer = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr[i][j] = -1
            answer.append(dfs(i,j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)