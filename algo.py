def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target: return m
        l, r = (m + 1, r) if arr[m] < target else (l, m - 1)
    return -1

print(f"Element found at index {binary_search([11, 5, 22, 34, 867], 867)}" if binary_search([11, 5, 22, 34, 867], 867) != -1 else "Element not found")


 