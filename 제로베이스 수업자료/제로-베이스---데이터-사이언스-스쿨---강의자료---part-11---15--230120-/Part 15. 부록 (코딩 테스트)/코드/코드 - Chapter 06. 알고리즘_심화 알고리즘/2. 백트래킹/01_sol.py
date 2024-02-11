def solution(N):
    result = []

    def dfs(path):
        def is_promising(path, n):
            new_i, new_j = len(path), n
            for i, j in enumerate(path):
                if new_j == j:
                    return False
                if new_i - i == abs(new_j - j):
                    return False
            return True

        if len(path) == N:
            result.append(path.copy())
            return
        
        for i in range(N):
            if is_promising(path, i):
                path += [i]
                dfs(path + [i])
                del path[-1]
    
    dfs([])
    return result


if __name__ == '__main__':
    N = 4
    sol = solution(N)
    print(sol)
