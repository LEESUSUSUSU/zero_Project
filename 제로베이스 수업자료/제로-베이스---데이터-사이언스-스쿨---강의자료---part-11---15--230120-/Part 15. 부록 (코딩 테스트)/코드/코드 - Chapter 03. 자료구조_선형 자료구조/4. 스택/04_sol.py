# Prob3.
# 후위표기법으로 표기된 계산식 s 연산하기
# 후위표기법: 피연산자가 2개 나온 후에 연산자가 나오는 표기법
#            ex) "4 2 +" -> 4 + 2 = 6
# 
# 입출력 예시)
# s = "2 4 +"
# 결과: 6
#
# s = "2 2 -"
# 결과: 0
#
# s = "1 3 + 5 * 2 * 5 +"
# 결과: 45
#


def solution(s):
    stack = []

    for c in s.split(' '):
        if c.isdigit():
            stack.append(int(c))
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if c == '+':
                stack.append(val1 + val2)
            elif c == '-':
                stack.append(val1 - val2)
            elif c == '*':
                stack.append(val1 * val2)
            elif c == '/':
                stack.append(val1 / val2)
    val = stack.pop()
    return val

if __name__ == '__main__':
    s = "1 3 + 5 * 2 * 5 +"
    sol = solution(s)
    print(sol)
