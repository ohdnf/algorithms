def insertion_sort(arr):
    for i in range(1, len(arr)):
        position = i
        tmp = arr[i]

        while position > 0 and arr[position - 1] > tmp:
            arr[position] = arr[position - 1]
            position -= 1
        
        arr[position] = tmp
    
    return arr


if __name__ == "__main__":
    a = [4, 2, 7, 3, 1]
    a = insertion_sort(a)
    print(a)