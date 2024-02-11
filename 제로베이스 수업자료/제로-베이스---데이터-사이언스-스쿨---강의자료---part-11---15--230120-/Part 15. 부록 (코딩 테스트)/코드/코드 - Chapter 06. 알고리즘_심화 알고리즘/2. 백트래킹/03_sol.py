def solution(s):
    result = []

    def dfs(path):
        if len(path) == 3:
            result.append(make_address(path))
            return
        
        for i in range(1, 4):
            if is_promising(path, i):
                path += [i]
                dfs(path)
                del path[-1]

    def is_promising(path, k):
        tokens = []
        if len(path) == 0:
            tokens.append(s[:k])
        elif len(path) == 1:
            start = path[0]
            tokens.append(s[start:start+k])
        else:
            start = sum(path)
            tokens.append(s[start:start+k])
            tokens.append(s[start+k:])

        for token in tokens:
            if len(token) == 0:
                return False
            if len(token) > 1 and token[0] == '0':
                return False
            if int(token) > 255:
                return False
        return True

    def make_address(path):
        tokens = []
        tokens.append(s[:path[0]])
        tokens.append(s[path[0]:path[0]+path[1]])
        tokens.append(s[path[0]+path[1]:path[0]+path[1]+path[2]])
        tokens.append(s[path[0]+path[1]+path[2]:])
        return '.'.join(tokens)
    
    dfs([])
    return result
    


if __name__ == '__main__':
    s = "11011"
    sol = solution(s)
    print(sol)
