import sys
import heapq

N,M = map(int, input().split())
array = list(map(int, input().split()))
pos,neg = [], []

# 가장 거리가 먼 책까지의 거리는?
largest = max(max(array), -min(array))
# print(largest)
# Max Heap을 위해 원소를 음수로 구성
for i in array:
    # 책 위치가 양수면
    if i > 0:
        heapq.heappush(pos, -i)
    else:
        heapq.heappush(neg, i)
# print(pos)
# print(neg)

result = 0


while pos:
    # 한번에 m개씩 옮길수 있으므로 m개씩 꺼내기
    t = heapq.heappop(pos)
    
    # print(f"heapq.heappop(pos) : {t}")
    
    result += t
    
    for _ in range(M-1):
        if pos:
            heapq.heappop(pos)
            
while neg:
    # 한번에 m개씩 옮길수 있으므로 m개씩 꺼내기
    t = heapq.heappop(neg)
    # print(f"heapq.heappop(neg) : {t}")
    result += t
    
    for _ in range(M-1):
        if neg:
            heapq.heappop(neg)
            
# print(result)
print(-result * 2 - largest)