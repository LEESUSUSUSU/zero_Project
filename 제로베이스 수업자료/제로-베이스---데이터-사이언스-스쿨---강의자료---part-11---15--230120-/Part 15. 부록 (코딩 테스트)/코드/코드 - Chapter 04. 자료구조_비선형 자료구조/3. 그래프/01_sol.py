class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        self.adj_list = adj_list if adj_list else []


class Graph:
    def __init__(self):
        self.vertices = []

    def insert(self, value, adj_list):
        self.vertices.append(Vertex(value, adj_list))
        for adj_ind in adj_list:
            self.vertices[adj_ind].adj_list.append(len(self.vertices) - 1)

    def bfs(self, vert_ind, value):
        visited = [False for _ in range(len(self.vertices))]
        queue = []
        queue.append(vert_ind)

        while queue:
            node_ind = queue.pop(0)
            
            if visited[node_ind]:
                continue
            
            visited[node_ind] = True

            node = self.vertices[node_ind]

            if node.value == value:
                return True
            
            for adj_ind in node.adj_list:
                queue.append(adj_ind)

        return False

    def dfs(self, vert_ind, value):
        is_found = False
        visited = [False for _ in range(len(self.vertices))]

        def recursive(node_ind):
            nonlocal is_found

            # 이미 value를 찾았으면 바로 종료
            if is_found:
                return
            
            # 이미 visit한 노드라면 종료
            if visited[node_ind]:
                return
            
            # 처음 방문하는 노드라면 visit을 True로 변경
            visited[node_ind] = True

            node = self.vertices[node_ind]

            # 현재 노드의 값이 찾고자 하는 value인지 검사
            if node.value == value:
                is_found = True
                return
            
            # 인접한 모든 노드를 재귀적으로 호출
            for adj_index in node.adj_list:
                recursive(adj_index)
        
        recursive(vert_ind)

        return is_found

graph = Graph()
graph.insert(0, [])
graph.insert(1, [0])
graph.insert(2, [1])
graph.insert(3, [2])
graph.insert(4, [0, 2, 3])

print(graph.bfs(0, 2))
print(graph.dfs(0, 3))