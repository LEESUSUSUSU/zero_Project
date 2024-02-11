class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def recursive(node):
            if node is None:
                return
            
            # 현재 노드 방문
            print(node.value, end=' ')

            # 왼쪽 자식 노드           
            recursive(node.left)

            # 오른쪽 자식 노드
            recursive(node.right)
        
        recursive(self.root)
        print()
    
    def inorder(self):
        def recursive(node):
            if node is None:
                return
            
            # 왼쪽 자식 노드           
            recursive(node.left)

            # 현재 노드 방문
            print(node.value, end=' ')

            # 오른쪽 자식 노드
            recursive(node.right)
        
        recursive(self.root)
        print()
    
    def postorder(self):
        def recursive(node):
            if node is None:
                return
            
            # 왼쪽 자식 노드           
            recursive(node.left)

            # 오른쪽 자식 노드
            recursive(node.right)

            # 현재 노드 방문
            print(node.value, end=' ')
        
        recursive(self.root)
        print()

    def levelorder(self):
        if self.root is None:
            return

        queue = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            
            # 큐에서 뽑은 노드를 방문
            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print()


    def bfs(self, value):
        if self.root is None:
            return

        queue = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            
            # 큐에서 뽑은 노드를 방문
            if node.value == value:
                return True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
                
        return False
    
    def dfs(self, value):
        is_found = False
        def recursive(node):
            nonlocal is_found

            if node is None:
                return

            if is_found:
                return
            
            # 현재 노드 방문
            if value == node.value:
                is_found = True
                return

            # 왼쪽 자식 노드           
            recursive(node.left)

            # 오른쪽 자식 노드
            recursive(node.right)
        
        recursive(self.root)
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