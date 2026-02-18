def binary_search(arr, key):
    low = 0
    up = len(arr) - 1
    
    while low <= up:
        mid = (low + up) // 2
        
        if arr[mid] == key:
            return mid  
        elif arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            up = mid - 1
        
    return -1