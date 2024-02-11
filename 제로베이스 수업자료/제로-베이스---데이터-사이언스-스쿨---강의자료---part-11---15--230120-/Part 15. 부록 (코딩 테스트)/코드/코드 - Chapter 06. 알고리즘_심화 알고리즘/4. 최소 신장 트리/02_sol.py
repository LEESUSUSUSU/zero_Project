from heapq import heappop, heappush

def solution(N, edge):
    visited = [False for _ in range(N+1)]
    start = 1

    heap = []
    visited[start] = True
    for a, b, w in filter(lambda x: x[0] == start or x[1] == start, edge):
        node = a if start == b else b
        heappush(heap, (w, node))
    
    mst_weight = 0
    while heap:
        w, node = heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        mst_weight += w

        for a, b, new_w in filter(lambda x: x[0] == node or x[1] == node, edge):
            new_node = a if node == b else b
            heappush(heap, (new_w, new_node))
    
    return mst_weight


if __name__ == '__main__':
    N = 5
    edge = [[1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6], [5, 1, 1]]
    sol = solution(N, edge)
    print(sol)
