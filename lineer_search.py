def lineer_research(arr, target):
    for index in range(0, len(arr)):
        if target == arr[index]:return index         
    return 1
    
arr = [4,2,7,6,8,3,5]
print(f"searching...\n target found in {lineer_research(arr, 6)} index" if lineer_research(arr, 6) != -1 else "target not found.")
