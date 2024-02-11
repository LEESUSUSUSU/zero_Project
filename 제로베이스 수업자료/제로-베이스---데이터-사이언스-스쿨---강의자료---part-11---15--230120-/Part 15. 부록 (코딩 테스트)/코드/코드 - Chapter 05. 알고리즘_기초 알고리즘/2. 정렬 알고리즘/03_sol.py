from functools import cmp_to_key


def solution(numbers):
    def compare(x, y):
        a = int(str(x) + str(y))
        b = int(str(y) + str(x))
        return 1 if b > a else -1
    key = cmp_to_key(compare)

    numbers.sort(key=key)
    return ''.join(map(str, numbers))


if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    sol = solution(numbers)
    print(sol)
