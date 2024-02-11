from heapq import heappush, heappop

def solution(x, y):
    n = len(x)
    root = list(range(n))
    rank = [1]*n

    def union(i, j):
        i_root = find(i)
        j_root = find(j)
        if i_root != j_root:
            if rank[i_root] >= rank[j_root]:
                root[j_root] = i_root
                rank[i_root] += rank[j_root]
            else:
                root[i_root] = j_root
                rank[j_root] += rank[i_root]
        
    def find(i):
        if i != root[i]:
            i = find(root[i])
        return root[i]
    
    def manhattan(i, j):
        return abs(x[i] - x[j]) + abs(y[i] - y[j])
        
    heap = []
    for i in range(n-1):
        for j in range(i+1, n):
            d = manhattan(i, j)
            heappush(heap, (d, i, j))
    
    total_dist = 0
    edges = []
    while len(edges) < n - 1:
        d, i, j = heappop(heap)
        if find(i) == find(j):
            continue
        union(i, j)
        edges.append((d, i, j))
        total_dist += d
    
    return total_dist
