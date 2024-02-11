def solution(image):
    def encode(i, j, n):
        if n == 1:
            return str(image[i][j])
        
        first_value = image[i][j]
        is_consistent = True
        for k in range(i, i+n):
            for l in range(j, j+n):
                if image[k][l] != first_value:
                    is_consistent = False
                    break
        
        if is_consistent:
            return str(first_value)
        
        s = '('
        s += encode(i, j, n // 2)
        s += encode(i, j + n // 2, n // 2)
        s += encode(i + n // 2, j, n // 2)
        s += encode(i + n // 2, j + n // 2, n // 2)
        s += ')'
        return s

    return encode(0, 0, len(image))


if __name__ == '__main__':
    image = [[0, 0, 0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1]]
    sol = solution(image)
    print(sol)
