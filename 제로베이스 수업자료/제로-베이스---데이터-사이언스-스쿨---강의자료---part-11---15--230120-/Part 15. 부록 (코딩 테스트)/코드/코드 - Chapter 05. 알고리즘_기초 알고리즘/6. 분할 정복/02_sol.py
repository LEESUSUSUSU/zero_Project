def solution(n, i, j):
    def solve(offset, n, i, j):
        if n == 2:
            mat = [[2, 1], [3, 4]]
            return offset + mat[i][j]
        
        m = n // 2
        m2 = m**2
        if i < m and j >= m:
            return solve(offset, m, i, j-m)
        elif i < m and j < m:
            return solve(offset + m2, m, i, j)
        elif i >= m and j < m:
            return solve(offset + 2*m2, m, i-m, j)
        else:
            return solve(offset + 3*m2, m, i-m, j-m)
    return solve(0, n, i, j)


if __name__ == '__main__':
    n = 4
    i = 1
    j = 3
    sol = solution(n, i, j)
    print(sol)
