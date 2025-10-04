# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n - 1, 1):
        for j in range(0, n - i - 1, 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr


arr = [7, 9, 3, 5, 4, 6]


print(bubble_sort(arr))