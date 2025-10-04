# duplicate 2
def duplicate2(arr):
    newArr = []
    for i in range(len(arr)):
        if(newArr[arr[i]] == 1):
            return True
        else:
            newArr[arr[i]] = 1
    return False