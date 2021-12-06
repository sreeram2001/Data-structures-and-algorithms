
''' Heap Sort is a Comparison - Based technique which is based on Binary heap. 
It gives a time-complexity of O(nlogn) in all cases. '''


def heapify(arr,i):
    parent = i
    left = 2*i + 1
    right = 2*i + 2
    
    
    if left < len(arr) and arr[parent] > arr[left]:
        parent = left
        
    if right < len(arr) and arr[parent] > arr[right]:
        parent = right
        
    if parent != i:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify(arr,parent)
        
    print(arr)


def heapsort(arr):
    
    for i in range(len(arr)-1,-1,-1):
        heapify(arr,i)
        
    print(arr)
    
    
#user-code
array = [12, 11, 13, 5, 6, 7]                                   #unsorted - input array
print(heapsort(array))                                          #call the function - also prints sorted array
