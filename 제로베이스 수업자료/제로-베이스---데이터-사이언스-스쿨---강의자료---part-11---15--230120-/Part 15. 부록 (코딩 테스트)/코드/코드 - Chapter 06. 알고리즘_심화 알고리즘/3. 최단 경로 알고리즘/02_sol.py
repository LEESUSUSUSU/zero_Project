from heapq import heappop, heappush


def solution(N, edge):
    start = 0
    dists = [float('inf') for _ in range(N)]
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
    
    max_val = max(dists)
    return dists.index(max_val)
    


if __name__ == '__main__':
    N = 5
    edge = [[0, 1, 5], [0, 2, 7], [1, 3, 10], [3, 4, 8], [2, 4, 9], [4, 2, 1]]
    sol = solution(N, edge)
    print(sol)
