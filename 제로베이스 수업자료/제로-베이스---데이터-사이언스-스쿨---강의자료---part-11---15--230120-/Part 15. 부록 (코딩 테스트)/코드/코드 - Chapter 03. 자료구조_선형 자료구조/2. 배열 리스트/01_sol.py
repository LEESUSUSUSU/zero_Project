# Prob1.
# 리스트 arr의 모든 자료에 대해서,
# 짝수 데이터들의 평균과 홀수 데이터들의 평균을 각각 계산하시오.
# 출력은 2개의 출력을 리스트로 묶어 출력하시오.
# 
# 입출력 예시)
# arr = [1, 3, 5, 7, 9, 2, 5, 1, 4]
# 결과: [3.25, 4.8]


def solution(arr):
    even_arr = arr[1::2]
    odd_arr = arr[::2]
    return [sum(even_arr) / len(even_arr),
            sum(odd_arr) / len(odd_arr)]


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 2, 5, 1, 4]
    sol = solution(arr)
    print(sol)
