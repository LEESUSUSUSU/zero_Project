# Prob4.
# 이차원 리스트 arr를 시계방향으로 90도 회전시킨 결과를 출력하시오.
# 
# 입출력 예시)
# arr = [[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15]]
# 결과: [[11, 6, 1],
#        [12, 7, 2],
#        [13, 8, 3],
#        [14, 9, 4]
#        [15, 10, 5]]


def solution(arr):
    N = len(arr)
    M = len(arr[0])
    
    res = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        for j in range(M):
            res[j][N-i-1] = arr[i][j]
    return res


if __name__ == '__main__':
    arr = [[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15]]
    sol = solution(arr)
    print(sol)
