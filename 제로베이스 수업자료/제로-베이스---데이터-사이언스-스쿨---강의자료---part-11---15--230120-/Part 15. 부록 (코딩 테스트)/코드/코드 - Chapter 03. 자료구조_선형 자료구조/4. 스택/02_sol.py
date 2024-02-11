# Prob1.
# 스택을 이용하여 문자열 s를 뒤집기
# 
# 
# 입출력 예시)
# s = "zerobase"
# 결과: "esaborez"


def solution(s):
    res = ""
    stack = []
    for c in s:
        stack.append(c)
    
    while stack:
        res += stack.pop()
    
    return res


if __name__ == '__main__':
    s = "zerobase"
    sol = solution(s)
    print(sol)
