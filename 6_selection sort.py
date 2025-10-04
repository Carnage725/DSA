# selection sort implementation
def selectionSort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        
        for j in range(i + 1, len(arr)):
            if arr[j] < min_idx:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr