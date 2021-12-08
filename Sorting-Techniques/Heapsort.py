''' Heap Sort is a Comparison - Based technique which is based on Binary heap. 
It gives a time-complexity of O(nlogn) in all cases. '''


def heapify(arr,ind):
    parent = ind
    left = 2*ind + 1
    right = 2*ind + 2
    
    if left < len(arr) and arr[parent] > arr[left]:
        parent = left
        
    if right < len(arr) and arr[parent] > arr[right]:
        parent = right
        
    if parent != ind:
        arr[parent], arr[ind] = arr[ind], arr[parent]
        heapify(arr,parent)
        
        
 
def heapsort(arr):
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,i)
        

    for i in range(len(arr)-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,0)
        
        
    return arr
    
    
    
#driver-code
arr = [6,4,3,2,7,9]
print(heapsort(arr))