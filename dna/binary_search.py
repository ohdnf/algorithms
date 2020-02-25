def binary_search(arr, val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if val < mid_val:
            right = mid - 1
        elif val > mid_val:
            left = mid + 1
        elif val == mid_val:
            return mid
    
    return None


if __name__ == "__main__":
    a = list(range(1, 10))
    b = binary_search(a, 7)
    print(b)