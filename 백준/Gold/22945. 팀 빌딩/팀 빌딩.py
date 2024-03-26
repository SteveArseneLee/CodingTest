n = int(input())
devs = list(map(int, input().split()))
L,R = 0, n-1
ans = 0

# 값은 (i~j)idx * min(arr[i],arr[j])

while (L<R):
    tmp = (R-L-1) * min(devs[R],devs[L])
    ans = max(ans, tmp)
    if devs[R] > devs[L]:
        L += 1
    else:
        R -= 1
print(ans)