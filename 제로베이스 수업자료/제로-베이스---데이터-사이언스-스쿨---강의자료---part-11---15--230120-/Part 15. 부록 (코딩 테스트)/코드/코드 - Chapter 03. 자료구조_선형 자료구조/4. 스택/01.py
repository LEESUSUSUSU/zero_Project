# Python에서 stack 사용하기 (리스트 응용)

stack = []

print(len(stack) == 0)  # is_empty()는 len(stack) == 0 으로 판단

for i in range(1, 11):
    stack.append(i)  # push()를 구한하고 있는 append

print(stack)
print(len(stack) == 0)  # is_empty()는 len(stack) == 0 으로 판단

print(stack[-1]) # peek()는 [-1]로 구현

for i in range(1, 11):
    val = stack.pop()  # pop()
    print(val, end=' ')
print()

print(len(stack) == 0)  # is_empty()는 len(stack) == 0 으로 판단