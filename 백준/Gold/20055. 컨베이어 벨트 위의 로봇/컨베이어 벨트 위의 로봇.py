import sys
si = sys.stdin.readline
# 원형 큐를 위해 deque 사용
from collections import deque

n, k = map(int, si().split())
belt = deque(list(map(int, si().split())))
robot = deque([False] * n)
result = 1 # 1단계부터 시작

while True:
    # 1. 벨트가 로봇과 함께 한칸 회전
    belt.rotate()
    robot.rotate()
    robot[n-1] = False # 내리는 위치에서 로봇 내리기
    # 2. 가장 먼저 벨트에 올라간 로봇부터
    # 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] >= 1:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
    robot[n-1] = False # 내리는 위치에서 로봇 내리기

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면
    # 올리는 위치에 로봇 올리기
    if belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1
    # 4. 내구도 0이 K개 이상이라면 종료
    if belt.count(0) >= k:
        break
    result += 1
print(result)