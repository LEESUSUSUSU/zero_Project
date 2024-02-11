def solution(depth, n, blocks):
    D = depth + 1
    N = len(blocks[0])

    dp = [[0 for _ in range(N)] for _ in range(2)]

    for i in range(N):
        dp[0][i] = blocks[0][i]
    
    for i in range(1, D):
        for j in range(N):
            if j == 0:
                dp[i%2][j] = min(dp[(i-1)%2][j:j+2]) + blocks[i][j]
            elif j == N-1:
                dp[i%2][j] = min(dp[(i-1)%2][j-1:j+1]) + blocks[i][j]
            else:
                dp[i%2][j] = min(dp[(i-1)%2][j-1:j+2]) + blocks[i][j]
    
    return dp[depth%2][n]

if __name__ == '__main__':
    depth = 3
    n = 3
    blocks = [[5, 6, 2, 6],
             [1, 6, 4, 9],
             [5, 6, 9, 4],
             [55, 14, 21, 14]]
    sol = solution(depth, n, blocks)
    print(sol)
