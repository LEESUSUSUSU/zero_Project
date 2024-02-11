# Trie를 자료구조를 구현하시오.

class Node:
    def __init__(self):
        self.children = dict()
    

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.children['*'] = Node()

    def search(self, query):
        curr = self.root
        for c in query:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return '*' in curr.children
            
trie = Trie()
words = ['abc', 'abcd', 'bcd', 'zzz', 'zz', 'zerobase', 'zero']
for word in words:
    trie.add_word(word)

queries = ['abc', 'ab', 'zz', 'zzzz', 'zero', 'zerob']
        #  True   False  True  False  True  False
result = []
for query in queries:
    result.append(trie.search(query))
print(result)