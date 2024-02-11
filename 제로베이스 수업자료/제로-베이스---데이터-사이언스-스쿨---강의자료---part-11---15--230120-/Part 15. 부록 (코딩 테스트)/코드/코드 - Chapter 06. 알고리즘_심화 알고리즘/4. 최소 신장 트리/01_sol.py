from heapq import heappop, heappush

def solution(N, edge):
    rank = [1 for _ in range(N+1)]
    parent = [i for i in range(N+1)]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return False
        
        if rank[x_root] < rank[y_root]:
            x_root, y_root = y_root, x_root
        
        parent[y_root] = x_root
        rank[x_root] += rank[y_root]
        return True
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    heap = []
    for a, b, w in edge:
        heappush(heap, (w, a, b))
    
    mst_weight = 0
    count = 0
    while heap:
        w, a, b = heappop(heap)
        if union(a, b):
            mst_weight += w
            count += 1
        if count == N:
            break
    
    return mst_weight


if __name__ == '__main__':
    N = 5
    edge = [[1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6], [5, 1, 1]]
    sol = solution(N, edge)
    print(sol)
