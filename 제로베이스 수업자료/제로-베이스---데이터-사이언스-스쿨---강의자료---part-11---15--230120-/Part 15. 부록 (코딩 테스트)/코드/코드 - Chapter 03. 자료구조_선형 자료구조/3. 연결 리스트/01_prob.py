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
        pass

    def prepend(self, value):
        pass

    def append(self, value):
        pass

    def set_head(self, index):
        pass

    def access(self, index):
        pass

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass

    def print(self):
        pass
