# Prob2.
# 리스트의 자료 순서를 거꾸로 변경하시오.
# 추가 리스트를 생성하지 말고, 주어진 리스트에서 in-place로 하시오.
# 
# 입출력 예시)
# arr = [1, 3, 5, 7, 9]
# 결과: [9, 7, 5, 3, 1]


def solution(arr):
    N = len(arr)
    for i in range(N // 2):
        arr[N-i-1], arr[i] = arr[i], arr[N-i-1]
    return arr


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 5]
    sol = solution(arr)
    print(sol)
