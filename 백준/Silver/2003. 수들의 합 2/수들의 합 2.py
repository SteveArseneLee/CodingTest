n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
L, R = 0, 0
sum_value = 0

while True:
    if sum_value >= m:
        sum_value -= arr[L]
        L += 1
    elif R == n:
        break
    else:
        sum_value += arr[R]
        R += 1

    if sum_value == m:
        cnt += 1

print(cnt)