def is_perfect(l):
    if not l: return True
    for i in range(len(l)-1):
        is_perfect = True
        if p[i] != p[i+1]*3 and p[i] != p[i+1]/2:
            is_perfect = False
            break

    return is_perfect


def remove_elements(elements, l):
    res = l.copy()
    for e in elements:
        res.pop(res.index(e))
    return res


def rec(initial_list, current_list):
    if len(current_list) == len(initial_list):
        return current_list

    list_without_current_list_elements = remove_elements(current_list, initial_list)
    for e in list_without_current_list_elements:
        if not current_list:
            perfect_list = rec(initial_list, [e])
            if perfect_list is not None: return perfect_list
        else:
            if e == current_list[-1]/3 or e == current_list[-1]*2:
                new_current_list = current_list.copy()
                new_current_list.append(e)
                perfect_list = rec(initial_list, new_current_list)
                if perfect_list is not None: return perfect_list


initial_list = list(map(int, input().split()))
perfect_list = rec(initial_list, [])
print(*perfect_list, sep=' ')
