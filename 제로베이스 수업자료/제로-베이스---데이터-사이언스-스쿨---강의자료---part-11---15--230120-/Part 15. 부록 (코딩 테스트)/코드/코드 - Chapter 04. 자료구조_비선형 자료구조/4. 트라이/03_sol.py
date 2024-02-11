# Prob2.
# 
# 와일드카드 검색기2
# 검색할 단어가 리스트 words에 주어져 있다.
# 이번에는 queries의 검색 단어가 와일드카드 ?를 포함하고 있다.
# 모든 검색 단어는 마지막에 최소 한개의 ?를 가지고 있으며,
# ?의 개수만큼 아무 문자나 매칭이 가능하다.
# 이 프로그램을 구현하시오.
# 
# 예시 입출력
# words = ["fast", "zero", "base", "study", "baseball", "steel"]
# queries = ["fa??", "ba??", "ze?", "st???", "z???"]
# 출력: [1, 1, 0, 2, 1]



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
    tries = dict()
    for word in words:
        n = len(word)
        if n not in tries:
            tries[n] = Trie()
        tries[n].add_word(word)
    
    result = []
    for query in queries:
        n = len(query)
        if n not in tries:
            result.append(0)
        else:
            q = query[:query.index('?')]
            result.append(tries[n].search(q))
    return result


if __name__ == '__main__':
    words = ["fast", "zero", "base", "study", "baseball", "steel"]
    queries = ["fa??", "ba??", "ze?", "st???", "z???"]
    sol = solution(words, queries)
    print(sol)
