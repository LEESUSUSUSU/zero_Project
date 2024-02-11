def solution(s, k):
    if k >= len(s):
        return "0"
    
    if k == 0:
        return s.lstrip('0')
    
    if s[1] == '0':
        return solution(s[1:].lstrip('0'), k-1)
    else:
        ind = 0
        for i in range(1, len(s)):
            if s[i-1] <= s[i]:
                ind = i
            else:
                break
        return solution(s[:ind] + s[ind+1:], k-1)


if __name__ == '__main__':
    s = "105990"
    k = 1
    sol = solution(s, k)
    print(sol)
