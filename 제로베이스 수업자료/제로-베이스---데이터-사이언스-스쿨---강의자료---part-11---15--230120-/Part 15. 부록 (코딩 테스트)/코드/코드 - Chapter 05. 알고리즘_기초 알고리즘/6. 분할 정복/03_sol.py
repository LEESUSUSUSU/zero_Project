def solution(nums):
    def solve(left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        sol_left = solve(left, mid)
        sol_right = solve(mid + 1, right)
        sol_mid = solve_mid(left, mid, right)
        return max(sol_left, sol_right, sol_mid)
    
    def solve_mid(left, mid, right):
        max_left = -float('inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            max_left = max(max_left, curr_sum)
        
        max_right = -float('inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            max_right = max(max_right, curr_sum)
        
        return max_left + max_right
    
    return solve(0, len(nums)-1)


if __name__ == '__main__':
    nums = [-5, 0, -3, 4, -1, 3, 1, -5, 8]
    sol = solution(nums)
    print(sol)
