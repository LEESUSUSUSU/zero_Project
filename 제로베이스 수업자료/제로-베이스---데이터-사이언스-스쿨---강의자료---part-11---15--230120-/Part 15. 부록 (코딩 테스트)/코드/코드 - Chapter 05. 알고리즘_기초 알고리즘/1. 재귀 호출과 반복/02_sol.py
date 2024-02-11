def solution(s):
    def solve(l, r, k):
        if l >= r:
            return 0
        
        if s[l] == s[r]:
            return solve(l+1, r-1, k)
        elif k > 0:
            if solve(l+1, r, k-1) == 0 or solve(l, r-1, k-1) == 0:
                return 1
        return 2
    
    return solve(0, len(s)-1, 1)


if __name__ == '__main__':
    s = 'abba'
    sol = solution(s)
    print(sol)

    s = 'summuus'
    sol = solution(s)
    print(sol)

    s = 'xabba'
    sol = solution(s)
    print(sol)

    s = 'xabbay'
    sol = solution(s)
    print(sol)

    s = 'comcom'
    sol = solution(s)
    print(sol)

    s = 'comwwmoc'
    sol = solution(s)
    print(sol)

    s = 'comwwtmoc'
    sol = solution(s)
    print(sol)
