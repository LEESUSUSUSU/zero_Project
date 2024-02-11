from heapq import heappush, heappop


def solution(x, y):
    N = len(x)
    start = 0

    visited = [False for _ in range(N)]
    
    heap = []
    visited[start] = True
    for i in range(N):
        if i == start:
            continue
        w = m_dist((x[start], y[start]), (x[i], y[i]))
        heappush(heap, (w, i))
    
    mst_weight = 0
    while heap:
        w, node = heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        mst_weight += w

        for i in range(N):
            if i == node:
                continue
            w = m_dist((x[node], y[node]), (x[i], y[i]))
            heappush(heap, (w, i))
            
    return mst_weight

def m_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


if __name__ == '__main__':
    x = [0, 0, 3, 3, 6]
    y = [0, 3, 1, 4, 3]
    sol = solution(x, y)
    print(sol)
