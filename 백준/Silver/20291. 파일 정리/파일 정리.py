import sys
si = sys.stdin.readline

arr = {}
for _ in range(int(si())):
    x,y = si().strip().split('.')
    # if x in arr:
    #     arr[x] += 1
    # else:
    #     arr[x] = 1
    if y in arr:
        arr[y] += 1
    else:
        arr[y] = 1

arr = sorted(arr.items())
for i,e in arr:
    print(i, e)