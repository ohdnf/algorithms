def linear_search(arr, val):
    for e in arr:
        if e == val:
            return val
        elif e > val:
            break
    return None