def insertion_sort(arr):
    for i in range(1, len(arr)):      
        key, j = arr[i], i-1 

        while j >= 0 and key < arr[j]:
            arr[j + 1], j = arr[j], j-1
           
        arr[j + 1] = key
    return arr

arr = [4,2,7,4,6,8,3,5]
print(insertion_sort(arr))