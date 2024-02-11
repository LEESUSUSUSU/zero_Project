def solution(n):
    if n == 0:
        return 1
    
    value = 0
    # C_{n+1} = sigma_{i=0}^{n} (C_{i} * C_{n-i})
    for i in range(n):
        value += solution(i) * solution(n-i-1)
    return value


if __name__ == '__main__':
    N = 7
    sol = solution(N)
    print(sol)
