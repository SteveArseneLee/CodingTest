import sys
si = sys.stdin.readline
n , m = map(int, si().split())
trees = list(map(int, si().split()))

# H 높이로 잘랐을 때, M만큼을 얻을 수 있으면 true
# 없으면 false를 return
def determination(H):
    sum = 0
    for x in trees:
        if x > H:
            sum += x - H
    # 자를 수 있다!
    return sum >= m

l, r, ans = 0, 2000000000, 0
while l <= r:
    mid = (l+r) // 2
    if determination(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)