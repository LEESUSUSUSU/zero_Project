def solution(s, t):
    if len(s) != len(t):
        return False
    
    s_sorted_list = sorted(list(s))
    t_sorted_list = sorted(list(t))
    
    for s_, t_ in zip(s_sorted_list, t_sorted_list):
        if s_ != t_:
            return False
    return True


if __name__ == '__main__':
    s = "imfinethankyou"
    t = "atfhinemnoyuki"
    sol = solution(s, t)
    print(sol)
