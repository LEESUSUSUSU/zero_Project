from heapq import heappop, heappush


def solution(N, edge, start):
    dists = [float('inf') for _ in range(N + 1)]
    heap = []

    heappush(heap, (0, start))
    dists[start] = 0

    while heap:
        d, node = heappop(heap)
        for _, adj_node, w in filter(lambda x: x[0] == node, edge):
            new_dist = d + w
            if new_dist < dists[adj_node]:
                dists[adj_node] = new_dist
                heappush(heap, (new_dist, adj_node))
    
    return dists[1:]



if __name__ == '__main__':
    N = 5
    edge = [[1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6], [4, 5, 1]]
    start = 1
    sol = solution(N, edge, start)
    print(sol)
