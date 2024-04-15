import sys
input = sys.stdin.readline

N = int(input())
statue = [*map(int, input().split())]

total_value = 0
cur_value = 0

# 왼쪽을 바라보는 동상 기준
for i in statue:
    if i == 1:
        cur_value += 1
    else:
        cur_value -= 1
    if cur_value < 0:
        cur_value = 0
    total_value = max(total_value, cur_value)

cur_value = 0
# 오른쪽 바로보는 동상 기준
for j in statue:
    if j == 2:
        cur_value += 1
    else:
        cur_value -= 1
    if cur_value < 0:
        cur_value = 0
    total_value = max(total_value, cur_value)
print(total_value)