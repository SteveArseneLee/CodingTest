import sys
si = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, si().split())

selected = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]

def rec_func(k):
    if k == m:
        for x in selected:
            print(str(x) + ' ')
        print('\n')
    else:
        for cand in range(1,n+1):
            if used[cand]:
                continue
            selected[k] = cand
            used[cand] = 1
            rec_func(k+1)
            selected[k] = 0
            used[cand] = 0
rec_func(0)