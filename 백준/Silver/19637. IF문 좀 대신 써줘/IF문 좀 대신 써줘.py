import sys
input = sys.stdin.readline

# 칭호의 개수 N, 캐릭터 개수 M
N, M = map(int, input().split())
chingho = [input().split() for _ in range(N)]
# test_case = [input() for _ in range(M)]

def bs(rank, cnt):
    start, end = 0, N-1
    res = 0
    while start <= end:
        mid = (start+end) // 2
        if int(rank[mid][1]) >= cnt:
            end = mid-1
            res = mid
        else:
            start = mid + 1
    return res

for _ in range(M):
    test_case = int(input())
    # print(f"'test_case : {test_case}', 'bs(chingho, test_case) : {bs(chingho, test_case)}',{chingho[bs(chingho, test_case)][0]}")
    print(chingho[bs(chingho, test_case)][0])
    