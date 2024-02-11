def solution(arr, target):
    N = len(arr)
    closest_diff = float('inf')
    closest_sum = 0

    arr.sort()

    for left in range(N - 2):
        mid = left + 1
        right = N - 1

        while mid < right:
            curr_sum = arr[left] + arr[mid] + arr[right]
            curr_diff = abs(target - curr_sum)

            if curr_diff < closest_diff:
                closest_diff = curr_diff
                closest_sum = curr_sum
            elif curr_diff == closest_diff and closest_sum > curr_sum:
                closest_sum = curr_sum
            
            if curr_sum < target:
                mid += 1
            elif curr_sum > target:
                right -= 1
            else:
                return target

    return closest_sum


if __name__ == '__main__':
    arr = [5, 2, 15, 3, 10, 12]
    target = 21
    sol = solution(arr, target)
    print(sol)
