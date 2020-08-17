def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i    

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (high + low) // 2
        if target == arr[middle]:
            return middle
        if target < arr[middle]:
            high = middle - 1
        if target > arr[middle]:
            low = middle + 1
    return -1  # not found
