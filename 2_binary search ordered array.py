# binary search ordered array
def binary_search(arr, key):
    lower = 0
    upper = len(arr) - 1
    
    while lower <= upper:
        mid = (lower + upper) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lower = mid + 1
        elif arr[mid] > key:
            upper = mid - 1
            
    return None