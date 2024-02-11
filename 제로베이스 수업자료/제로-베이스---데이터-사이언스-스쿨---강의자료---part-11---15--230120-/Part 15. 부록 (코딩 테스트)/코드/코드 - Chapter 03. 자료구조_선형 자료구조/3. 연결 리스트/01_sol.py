# 연결리스트를 구현하고, 연결리스트의 기능을 테스트하세요!
# 아래 제공된 기본 틀을 이용하여 구현하세요.

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        # 1. 일반적인 경우에 잘 동작 하는가?
        # 2. 처음에 연결리스트가 비어있을 떄 잘 동작 하는가?
        node = Node(value, self.head)
        self.head = node

    def append(self, value):
        # 1. 일반적인 경우에 잘 동작 하는가?        
        curr = self.head

        if curr is None:
            # 2. 처음에 연결리스트가 비어있을 떄 잘 동작 하는가?
            self.head = Node(value, None)
            return

        while curr.next is not None:
            curr = curr.next
        node = Node(value, None)
        curr.next = node

    def set_head(self, index):
        # 1. 일반적인 경우에 잘 동작 하는가?
        curr = self.head
        for _ in range(index):
            # 2. index > N
            if curr is None:
                return
            curr = curr.next
        # 3. index == N
        if curr is None:
            return
        self.head = curr

    def access(self, index):
        # 1. 일반적인 경우에 잘 동작 하는가?
        curr = self.head
        for _ in range(index):
            # 2. index > N
            if curr is None:
                return None
            curr = curr.next
        # 3. index == N
        if curr is None:
            return None
        return curr.value

    def insert(self, index, value):
        # 2. 0번 인덱스에 삽입하는 경우
        if index == 0:
            self.prepend(value)
            return

        # 1. 일반적인 경우
        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return
            prev = curr
            curr = curr.next
        node = Node(value, curr)
        prev.next = node

    def remove(self, index):
        # 3. 비어있는 연결리스트에 적용하는 경우
        if self.head is None:
            return

        # 2. index = 0인 경우
        if index == 0:
            self.head = self.head.next
            return

        # 1. 일반적인 경우
        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return
            prev = curr
            curr = curr.next
        
        # 4. index == N인 경우
        if curr is None:
            return

        prev.next = curr.next

    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.value, end=' ')
            curr = curr.next
        print()



if __name__ == '__main__':
    my_list = LinkedList()
    my_list.print()

    for i in range(10):
        my_list.append(i + 1)

    my_list.print()

    for i in range(10):
        my_list.prepend(i + 1)

    my_list.print()

    value = my_list.access(3)
    print('my_list.access(3) = ' + str(value))

    my_list.insert(8, 128)
    my_list.print()

    my_list.remove(4)
    my_list.print()

    my_list.set_head(10)
    my_list.print()