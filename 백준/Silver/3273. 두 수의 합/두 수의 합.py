n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
L,R,cnt = 0,n-1,0

while L<R:
    sum_value = arr[L] + arr[R]
    if sum_value == x:
        cnt += 1
    if sum_value > x:
        R -= 1
    else: L += 1
print(cnt)