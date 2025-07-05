def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for a in range(i + 1, n):
            if arr[min_index] > arr[a]:
                min_index = a
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
        
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))