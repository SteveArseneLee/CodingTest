import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# n개의 숫자
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]
# print(dp)
# dp[i]는 0부터 i번째까지의 합
# 결국 3부터 5번째를 구하고 싶으면 dp[5]에 dp[2]를 빼야함
# dp[i] - dp[j-1]
for _ in range(m):
    x,y = map(int, input().split())
    i, j = x-1, y-1
    # print(dp[y-1] - dp[x-1])
    if i == 0: print(dp[j])
    else: print(dp[j] - dp[i-1])