import sys
si = sys.stdin.readline

# 센서 개수 N
n = int(si())
# 집중국 개수
k = int(si())

# 집중국 개수가 센서보다 많으면, 각 센서 위치에 설치하면 되므로 0
if k >= n:
    print(0)
    sys.exit()

# n개의 센서의 좌표가 한 개의 정수로 n개
array = list(map(int, si().split()))
array.sort()

# 간격을 본다
distances = []
for i in range(1, n):
    distances.append(array[i] - array[i-1])
distances.sort(reverse=True)

# print(distances)

# 덩어리가 k개면 됨. 가장 먼 간격부터 하나씩 지우고 k개까지만 남기기
for i in range(k-1):
    distances[i] = 0
print(sum(distances))