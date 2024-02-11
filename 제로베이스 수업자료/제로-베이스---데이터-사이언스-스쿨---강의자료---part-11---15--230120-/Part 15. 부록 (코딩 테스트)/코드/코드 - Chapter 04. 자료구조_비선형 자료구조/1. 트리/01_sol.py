class BinaryTree:
    def __init__(self, data):
        self.data = [-1] + data  # 첫번째 노드가 인덱스 1로 시작

    def preorder(self):
        def recursive(node):
            if node >= len(self.data):
                return

            # 현재 노드를 방문
            print(self.data[node], end=' ')

            # 좌측 자식 방문
            recursive(2*node)

            # 우측 자식 방문
            recursive(2*node + 1)
        
        recursive(1)
        print()

    def inorder(self):
        def recursive(node):
            if node >= len(self.data):
                return

            # 좌측 자식 방문
            recursive(2*node)

            # 현재 노드를 방문
            print(self.data[node], end=' ')

            # 우측 자식 방문
            recursive(2*node + 1)
        
        recursive(1)
        print()

    def postorder(self):
        def recursive(node):
            if node >= len(self.data):
                return

            # 좌측 자식 방문
            recursive(2*node)

            # 우측 자식 방문
            recursive(2*node + 1)

            # 현재 노드를 방문
            print(self.data[node], end=' ')
        
        recursive(1)
        print()

    def levelorder(self):
        # 배열로 표현된 완전이진트리는 이미 레벨오더 순회 순서로 되어 있다.
        for value in self.data[1:]:
            print(value, end=' ')
        print()
    
    def bfs(self, value):
        for elem in self.data[1:]:
            if value == elem:
                return True
        return False

    def dfs(self, value):
        is_found = False
        def recursive(node):
            nonlocal is_found

            if node >= len(self.data):
                return

            # value를 이미 찾았다면, 추가 탐색 불필요
            if is_found:
                return

            # 현재 노드를 방문
            if self.data[node] == value:
                is_found = True
                return

            # 좌측 자식 방문
            recursive(2*node)

            # 우측 자식 방문
            recursive(2*node + 1)
        
        recursive(1)
        return is_found


tree = BinaryTree([i for i in range(13)])
tree.preorder()
tree.inorder()
tree.postorder()
tree.levelorder()

print(tree.dfs(15))
print(tree.dfs(11))

print(tree.bfs(6))
print(tree.bfs(17))