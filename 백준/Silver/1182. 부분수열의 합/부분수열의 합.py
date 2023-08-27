import sys
n, S = map(int, sys.stdin.readline().split(' '))
nums = list(map(int, sys.stdin.readline().split(' ')))
ans = 0

def rec_func(k, value):
    if k == n:
        global ans
        if value == S:
            ans += 1

    else:
        rec_func(k + 1, value + nums[k])
        rec_func(k + 1, value)

rec_func(0, 0)
# 진부분집합인지 확인여부
if S == 0:
    ans -= 1
print(ans)