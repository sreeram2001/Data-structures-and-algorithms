
def heapify(arr,l,ind):
    parent = ind
    left = 2*ind + 1
    right = 2*ind + 2
    
    if left < l and arr[left] < arr[parent]:
        parent = left
        
    if right < l and arr[right] < arr[parent]:
        parent = right
        
    if ind != parent:
        arr[parent], arr[ind] = arr[ind], arr[parent]
        heapify(arr,l,parent)
        


def heapsort(arr):
    
    for i in range(len(arr)-1,-1,-1):
        heapify(arr,len(arr),i)
    
    return arr
    
#user-code
arr = [12, 11, 13, 5, 6, 7]
print(heapsort(arr))