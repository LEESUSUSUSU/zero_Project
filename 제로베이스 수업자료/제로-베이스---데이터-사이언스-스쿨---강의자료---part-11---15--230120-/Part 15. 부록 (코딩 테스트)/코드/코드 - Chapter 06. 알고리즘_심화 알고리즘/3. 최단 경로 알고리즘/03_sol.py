from heapq import heappush, heappop


def solution(N, flight, a, b, k):
    adj_lists = [[] for _ in range(N)]
    for src, dst, price in flight:
        adj_lists[src].append((dst, price))
    
    best_cnt = [float('inf') for _ in range(N)]
    heap = []
    heappush(heap, (0, 0, a))

    while heap:
        price, count, node = heappop(heap)

        if best_cnt[node] < count:
            continue

        best_cnt[node] = count

        if count > k:
            continue

        if node == b:
            return price
        
        for adj_node, add_price in adj_lists[node]:
            heappush(heap, (price + add_price, count + 1, adj_node))

    return -1


if __name__ == '__main__':
    N = 4
    flight = [[0, 2, 1], [1, 3, 20], [1, 0, 8], [2, 3, 1], [0, 3, 3]]
    a = 1
    b = 3
    k = 2
    sol = solution(N, flight, a, b, k)
    print(sol)
