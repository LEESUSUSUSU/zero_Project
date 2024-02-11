# 인접 리스트로 그래프의 bfs와 dfs를 구현하시오.

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
        return False

    def dfs(self, vert_ind, value):
        return False