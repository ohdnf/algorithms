class SortableArray:
    def __init__(self, array):
        self.array = array
    
    def partition(self, left, right):
        pivot_idx = right
        pivot_val = self.array[pivot_idx]
        
        right -= 1

        while True:
            while self.array[left] < pivot_val:
                left += 1

            while self.array[right] > pivot_val:
                right -= 1

            if left >= right:
                break
            else:
                self.swap(left, right)
        
        self.swap(left, pivot_idx)

        return left
    
    def swap(self, first, second):
        self.array[first], self.array[second] = self.array[second], self.array[first]

    def quick_sort(self, left, right):
        if right <= left:
            return
        
        pivot = self.partition(left, right)
        self.quick_sort(left, pivot-1)
        self.quick_sort(pivot+1, right)
    
    def quick_select(self, kth_lowest_value, left, right):
        if right <= left:
            return self.array[left]
        
        pivot = self.partition(left, right)

        if kth_lowest_value == pivot:
            return self.array[pivot]
        elif kth_lowest_value < pivot:
            return self.quick_select(kth_lowest_value, left, pivot-1)
        elif kth_lowest_value > pivot:
            return self.quick_select(kth_lowest_value, pivot+1, right)
        
        

if __name__ == "__main__":
    # arr = [0, 5, 2, 1, 6, 3]
    # sortable_array = SortableArray(arr)
    # sortable_array.quick_sort(0, len(arr)-1)
    # print(sortable_array.array)

    arr = [0, 50, 20, 10, 60, 30]
    sortable_array = SortableArray(arr)
    val = sortable_array.quick_select(2, 0, len(arr)-1)
    print(val)
    