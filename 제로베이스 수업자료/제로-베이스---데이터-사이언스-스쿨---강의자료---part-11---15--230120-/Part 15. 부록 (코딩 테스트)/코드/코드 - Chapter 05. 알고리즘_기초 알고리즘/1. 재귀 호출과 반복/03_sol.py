def solution(n):
    def solve(n, start, end, temp):
        if n == 1:
            return [[start, end]]
        
        return solve(n-1, start, temp, end) + [[start, end]] + solve(n-1, temp, end, start)

    return solve(n, 1, 3, 2)


if __name__ == '__main__':
    n = 3
    sol = solution(n)
    print(sol)
