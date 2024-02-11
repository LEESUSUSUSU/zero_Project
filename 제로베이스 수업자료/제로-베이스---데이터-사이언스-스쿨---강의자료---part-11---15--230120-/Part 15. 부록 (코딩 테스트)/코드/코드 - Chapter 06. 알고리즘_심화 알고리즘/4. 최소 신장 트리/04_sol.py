def solution(N, graph, infected):
    rank = [1 for _ in range(N)]
    parent = [i for i in range(N)]

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
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                union(i, j)
    
    infected.sort()

    comps = dict()
    for i in infected:
        root = find(i)
        if root not in comps:
            comps[root] = []
        comps[root].append(i)
    
    max_ind = -1
    max_size = -1
    for i in infected:
        root = find(i)
        current_size = rank[root]

        if len(comps[root]) > 1:
            current_size = 0
        if current_size > max_size:
            max_ind = i
            max_size = current_size
    
    return max_ind


if __name__ == '__main__':
    N = 3
    graph = [[1, 1, 0],
            [1, 1, 0],
            [0, 0, 1]]
    infected = [0, 2]
    sol = solution(N, graph, infected)
    print(sol)
