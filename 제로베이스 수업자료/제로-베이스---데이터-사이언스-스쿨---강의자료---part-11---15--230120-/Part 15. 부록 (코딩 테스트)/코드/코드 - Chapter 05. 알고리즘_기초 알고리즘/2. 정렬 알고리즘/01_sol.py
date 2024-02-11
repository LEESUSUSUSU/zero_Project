def solution(grade, class_name, score):
    items = [(g, c, -s, s) for g, c, s in zip(grade, class_name, score)]
    items.sort()
    return list(map(lambda x: x[-1], items))


if __name__ == '__main__':
    grade = [3, 2, 1, 2, 1, 3, 2]
    class_name = [1, 3, 2, 3, 1, 3, 3]
    score = [50, 40, 66, 80, 100, 42, 99]
    sol = solution(grade, class_name, score)
    print(sol)
