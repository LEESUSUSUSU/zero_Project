def solution(ingredients, items):
    buy_dict = dict()
    left, right = 0, 0
    result = len(items)

    set_a = set(ingredients)
    buy_dict[items[left]] = 1
    if set_a.issubset(buy_dict.keys()):
        result = 1
        return result
    
    while left <= right:  # O(N)
        if set_a.issubset(buy_dict.keys()):
            result = min(result, right - left + 1)

            if buy_dict[items[left]] == 1:
                del buy_dict[items[left]]
            else:
                buy_dict[items[left]] -= 1

            left += 1
        else:
            right += 1

            if right == len(items):
                break

            if items[right] in buy_dict:
                buy_dict[items[right]] += 1
            else:
                buy_dict[items[right]] = 1
    
    return result
            

    



if __name__ == '__main__':
    ingredients = ["생닭", "인삼", "소주", "대추"]
    items = ["물", "인삼", "커피", "생닭", "소주", "사탕", "생닭", "대추", "쌀"]
    sol = solution(ingredients, items)
    print(sol)
