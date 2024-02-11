# Prob2.
# 괄호 짝이 잘 맞는지 검사하기
# 입력받은 문자열 s의 괄호가
# 올바른 짝이면 True, 아니면 False
# 
# 입출력 예시)
# s = "(())"
# 결과: True
#
# s = "(()"
# 결과: False
#
# s = "()()()"
#
# 결과: True


def solution(s):
    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    s = "(()(()))()"
    sol = solution(s)
    print(sol)
