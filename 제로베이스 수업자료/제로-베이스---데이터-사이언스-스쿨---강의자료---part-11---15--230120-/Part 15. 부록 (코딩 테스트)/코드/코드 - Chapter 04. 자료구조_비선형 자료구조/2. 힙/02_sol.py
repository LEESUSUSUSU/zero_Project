# Prob1.
# 
# 슬라이딩 최댓값
# 리스트 arr에 정수로 이루어진 자료가 주어져 있다.
# 이 때, 연속된 k개 중 최댓값을 구하고 싶다.
# 예를 들어, arr = [1, 3, 5, 2, 7, 4]이고 k = 3이라면
# 
# 첫번째 최댓값은 max([1, 3, 5]) -> 5
# 두번째 최댓값은 max([3, 5, 2]) -> 5
# 세번째 최댓값은 max([5, 2, 7]) -> 7
# 네번째 최댓값은 max([2, 7, 4]) -> 7
# 
# 따라서 결과는 [5, 5, 7, 7]이 된다.
# 
# 이 프로그램을 구현하시오.

from heapq import heapify, heappush

def solution(arr, k):
    result = []
    window = list(map(lambda x: -x, arr[:k]))
    heapify(window)  # 이거 필수!!!
    result.append(-window[0])

    for i in range(len(arr) - k):
        window.remove(-arr[i])
        heapify(window)  # 이거 필수!!!
        heappush(window, -arr[i+k])
        result.append(-window[0])

    return result


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 7, 4]
    k = 3
    sol = solution(arr, k)
    print(sol)
