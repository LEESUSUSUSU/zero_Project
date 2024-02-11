def solution1(arr, target):
    left = 0
    right = len(arr) - 1    

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


def solution2(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        return solution2(arr, target, left, mid-1)
    else:
        return solution2(arr, target, mid+1, right)



if __name__ == '__main__':
    arr = [10, 20, 40, 50, 60, 70]
    target = 40

    sol = solution1(arr, target)
    print(sol)

    sol = solution2(arr, target)
    print(sol)
