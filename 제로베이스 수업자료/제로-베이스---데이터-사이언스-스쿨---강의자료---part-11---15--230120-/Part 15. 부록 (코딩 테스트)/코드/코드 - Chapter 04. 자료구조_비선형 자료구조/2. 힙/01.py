from heapq import heappop, heappush, heapify

# heapq 패키지를 이용한 min heap 사용법
heap = []
for elem in [4, 10, 8, 0, 10, 9, 2]:
    heappush(heap, elem)
print(heap)

while heap:
    data = heappop(heap)
    print(data, end=' ')
print()


# heapq 패키지를 이용한 max heap 사용법
heap = []
for elem in [4, 10, 8, 0, 10, 9, 2]:
    heappush(heap, -elem)
print(heap)

while heap:
    data = -heappop(heap)
    print(data, end=' ')
print()


# heapq 패키지를 이용한 priority queue 사용법
pq = []
            # (우선순위(작을수록 높음), 값)
for elem in [(1, 10), (4, 14), (-2, 5), (10, 6)]:
    heappush(pq, elem)

while pq:
    data = heappop(pq)
    print(data[1], end=' ')
print()


# heapify를 사용하는 방법: 일반적인 배열(리스트)를 힙으로 변경
heap = [4, 10, 8, 0, 10, 9, 2]
heapify(heap)
while heap:
    data = heappop(heap)
    print(data, end=' ')
print()