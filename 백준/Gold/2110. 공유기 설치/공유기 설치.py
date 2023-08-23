n, c = list(map(int, input().split()))

# 집 데이터
array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

# 집 사이의 최소, 최대 거리
start = 1
end = array[-1] - array[0]
result = 0

while (start <= end):
    mid = (start+end) // 2
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value+mid:
            value = array[i]
            count += 1
    # C개 이상의 공유기를 설치할 수 있는 경우
    if count >= c:
        start = mid+1
        result = mid
    # C개 이상 설치할 수 없는 경우
    else:
        end = mid - 1
print(result)