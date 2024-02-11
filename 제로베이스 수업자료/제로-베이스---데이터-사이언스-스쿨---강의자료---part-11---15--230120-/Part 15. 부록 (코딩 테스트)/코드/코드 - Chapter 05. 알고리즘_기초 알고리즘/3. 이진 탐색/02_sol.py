def solution(weights, delivery):
    left = max(weights)
    right = sum(weights)
    answer = float('inf')

    while left < right:
        mid = (left + right) // 2

        days = 1
        current_weight = 0
        for w in weights:
            if current_weight + w > mid:
                days += 1
                current_weight = 0
            current_weight += w
        
        if days > delivery:
            left = mid + 1
        else:
            answer = min(answer, mid)
            right = mid - 1
            
    return answer


if __name__ == '__main__':
    weights = [3, 2, 2, 4, 1, 4]
    delivery = 3
    sol = solution(weights, delivery)
    print(sol)
