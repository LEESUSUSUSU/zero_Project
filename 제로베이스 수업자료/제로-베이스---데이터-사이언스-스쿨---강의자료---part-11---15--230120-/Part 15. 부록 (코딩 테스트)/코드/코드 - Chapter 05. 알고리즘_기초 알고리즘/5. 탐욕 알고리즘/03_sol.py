def solution(num):
    digits = list(map(int, list(str(num))))

    inc_ind = -1
    for i in range(1, len(digits)):
        if digits[i] > digits[i-1]:
            inc_ind = i
            break
    
    if inc_ind == -1:
        return num
    
    max_val = digits[inc_ind]
    max_ind = inc_ind
    for i in range(inc_ind + 1, len(digits)):
        if digits[i] >= max_val:
            max_val = digits[i]
            max_ind = i
    
    for i in range(inc_ind):
        if digits[i] < max_val:
            digits[max_ind], digits[i] = digits[i], digits[max_ind]
            return int(''.join(map(str, digits)))


if __name__ == '__main__':
    num = 43824
    sol = solution(num)
    print(sol)
