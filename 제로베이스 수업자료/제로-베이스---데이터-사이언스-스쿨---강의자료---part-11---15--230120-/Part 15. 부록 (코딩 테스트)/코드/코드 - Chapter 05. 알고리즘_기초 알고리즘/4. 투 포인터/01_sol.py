def solution(s):
    return ' '.join(list(filter(len, s.split(' ')))[::-1])


if __name__ == '__main__':
    s = "  the sky   is    blue"
    sol = solution(s)
    print(sol)
