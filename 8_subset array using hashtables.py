# subset array using hashtables
def isSubset(arr1, arr2):
    smaller = []
    larger = []
    hashTable = {}
    
    if(len(arr1) > len(arr2)):
        smaller = arr2
        larger = arr1
    else:
        smaller = arr1
        larger = arr2
        
    for value in larger:
        hashTable[value] = True
    
    for value in smaller:
        if(hashTable[value] != True):
            return False
                
    return True
