# Prob3.
# 철수와 영희는 눈을 가리고 잡기 놀이를 하기로 했다.
# 철수는 도망치는 역할을 맡았으며, (x1, y1) 좌표에서 출발한다.
# 매 1초마다 철수는 동/서/남/북 중 한군데를 임의로 선택하여 이동한다.
# 영희는 철수를 잡는 역할을 맡았으며, (x2, y2) 좌표에서 출발한다.
# 매 1초마다 영희는 북서/북동/남서/남동 중 한군데를 임의로 선택하여 이동한다.
# 모든 경우 중에서, 영희가 철수를 가장 빨리 잡는 경우 몇 초의 시간이 걸리는지 출력하시오.
#
# 입력설명
# -1000 <= x1 <= 1000
# -1000 <= y1 <= 1000
# -1000 <= x2 <= 1000
# -1000 <= y2 <= 1000
#
# 입출력 예시
# x1 = 2
# y1 = 4
# x2 = 5
# y2 = -3
# 출력: 4

def solution(x1, y1, x2, y2):
    set_a = {(x1, y1)}
    set_b = {(x2, y2)}

    a_history = set()
    b_history = set()

    a_history.update(set_a)
    b_history.update(set_b)

    move_a = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    move_b = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    t = 0
    while True:
        t += 1

        next_set_a = set()
        next_set_b = set()

        for x, y in set_a:
            for dx, dy in move_a:
                pos = (x + dx, y + dy)
                if pos in a_history:
                    continue
                next_set_a.add((x + dx, y + dy))

        for x, y in set_b:
            for dx, dy in move_b:
                pos = (x + dx, y + dy)
                if pos in next_set_a:
                    return t
                if pos in b_history:
                    continue
                next_set_b.add((x + dx, y + dy))
        
        set_a = next_set_a
        set_b = next_set_b

        a_history.update(set_a)
        b_history.update(set_b)


if __name__ == '__main__':
    x1 = 2
    y1 = 4
    x2 = 5
    y2 = -3
    sol = solution(x1, y1, x2, y2)
    print(sol)
