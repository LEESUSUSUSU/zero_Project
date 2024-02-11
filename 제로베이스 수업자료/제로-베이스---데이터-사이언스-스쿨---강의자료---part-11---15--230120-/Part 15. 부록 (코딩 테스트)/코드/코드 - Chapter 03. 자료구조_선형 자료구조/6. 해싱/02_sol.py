# Prob2.
# 정수로 이루어진 리스트 arr에서,
# 총 합이 0이 되는 부분 리스트가 있는지 여부를 출력하시오.
# 부분 리스트란, 리스트의 일부 연속된 부분을 잘라 만든 리스트를 말한다.
#
# 예시 입출력
# arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
# 출력: True
#


def solution(arr):
    s = set()
    s.add(0)

    total = 0
    for elem in arr:
        total += elem
        # 장점1. total이 자주 중복되면 중복없이 하나로 해결된다.
        # 장점2. total in s 라는 탐색 연산이 O(1)로 동작
        if total in s:
            return True
        s.add(total)

    return False



if __name__ == '__main__':
    arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    sol = solution(arr)
    print(sol)
