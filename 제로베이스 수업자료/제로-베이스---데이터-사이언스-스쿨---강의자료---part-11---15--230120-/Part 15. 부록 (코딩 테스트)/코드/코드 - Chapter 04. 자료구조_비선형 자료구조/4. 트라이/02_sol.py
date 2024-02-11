# Prob1.
# 
# 와일드카드 검색기
# 검색할 단어가 리스트 words에 주어져 있다.
# 이 words에 queries에 있는 단어로 시작하는 단어를 모두 찾으려 한다.
# 예를 들어, words = ["buy", "bull", "bucket", "bill"] 일 때,
# "bu"를 검색하면 "bu"로 시작하는 단어 "buy", "bull", "bucket"이 일치하여 답은 3이 된다.
# 이 프로그램을 구현하시오.
# 
# 예시 입출력
# words = ["fast", "zero", "base", "study", "baseball", "steel"]
# queries = ["fa", "ba", "zer", "st", "sti"]
# 출력: [1, 2, 1, 2, 0]


class Node:
    def __init__(self):
        self.children = dict()
        self.count = 0
    

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        curr = self.root
        for c in word:
            curr.count += 1
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.children['*'] = Node()

    def search(self, query):
        curr = self.root
        for c in query:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count
            

def solution(words, queries):
    trie = Trie()
    for word in words:
        trie.add_word(word)
    
    result = []
    for query in queries:
        result.append(trie.search(query))
    return result


if __name__ == '__main__':
    words = ["fast", "zero", "base", "study", "baseball", "steel"]
    queries = ["fa", "ba", "zer", "st", "sti"]
    sol = solution(words, queries)
    print(sol)
