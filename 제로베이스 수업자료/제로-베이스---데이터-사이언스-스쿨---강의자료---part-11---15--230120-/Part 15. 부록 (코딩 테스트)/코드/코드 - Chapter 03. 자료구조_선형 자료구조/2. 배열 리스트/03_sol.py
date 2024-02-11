# Prob3.
# 리스트 arr에 존재하는 모든 피크 값을 출력하시오.
# 단, 피크 인덱스란
# 
# arr[i-1] < arr[i], arr[i+1] < arr[i]
# 
# 를 동시에 만족하는 인덱스 i를 말하며,
# 피크 값은 이 떄 arr[i]를 말한다.
# 
# 입출력 예시)
# arr = [3, 1, 2, 6, 2, 2, 5, 1, 9, 10, 1, 11]
# 결과: [6, 5, 10]


def solution(arr):
    res = []
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
            res.append(arr[i])
    return res


if __name__ == '__main__':
    arr = [3, 1, 2, 6, 2, 2, 5, 1, 9, 10, 1, 11]
    sol = solution(arr)
    print(sol)
