# linear search ordered array
def linear_search(arr, key):
    i = 0
    for num in arr:
        if num == key:
            return i
        elif num > key:
            break
        i += 1
    
    return None
