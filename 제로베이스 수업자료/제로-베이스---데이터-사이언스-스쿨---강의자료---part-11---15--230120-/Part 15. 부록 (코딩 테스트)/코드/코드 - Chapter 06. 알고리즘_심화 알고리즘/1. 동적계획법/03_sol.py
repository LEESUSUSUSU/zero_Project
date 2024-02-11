def solution(N, rewards):
    # 0번째를 선택할 수도 있으면, N-1번째는 없다 친다.
    dp = [0 for _ in range(N-1)]
    dp[0] = rewards[0]
    dp[1] = max(dp[0], rewards[1])
    for i in range(2, N-1):
        dp[i] = max(dp[i-1], dp[i-2] + rewards[i])
    answer = dp[N-2]

    # 0번째를 선택하지 않고, N-1번째를 선택할 수 있게 한다.
    dp = [0 for _ in range(N)]
    dp[0] = 0
    dp[1] = rewards[1]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + rewards[i])
    
    return max(answer, dp[N-1])


if __name__ == '__main__':
    N = 6
    rewards = [5, 10, 5, 7, 5, 9]
    sol = solution(N, rewards)
    print(sol)
