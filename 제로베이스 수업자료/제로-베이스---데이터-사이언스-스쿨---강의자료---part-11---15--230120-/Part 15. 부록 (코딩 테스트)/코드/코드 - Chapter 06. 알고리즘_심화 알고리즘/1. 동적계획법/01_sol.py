def solution(capacity, weight, value):
    N = len(weight)
    C = capacity
    dp = [[0 for _ in range(C+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for w in range(1, C+1):
            if w >= weight[i-1]:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[N][C]


if __name__ == '__main__':
    capacity = 20
    weight = [4, 5, 2, 3, 6, 8, 5, 5]
    value = [5, 2, 6, 7, 1, 3, 4, 6]
    sol = solution(capacity, weight, value)
    print(sol)
