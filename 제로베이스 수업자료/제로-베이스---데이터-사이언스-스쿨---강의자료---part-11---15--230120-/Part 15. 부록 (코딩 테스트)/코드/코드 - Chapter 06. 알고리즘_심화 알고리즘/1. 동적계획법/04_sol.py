def solution(nums):
    N = len(nums)
    max_reach = 0

    for i in range(N):
        if max_reach >= i:
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= N-1:
                return True
    return False


if __name__ == '__main__':
    nums = [3, 4, 1, 1, 0, 3]
    sol = solution(nums)
    print(sol)
