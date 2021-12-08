
def partition(arr,low,high):                    #pivot-partition-index
    
    pivot = arr[high]                           #set pivot initially as last element
    i = low - 1
    
    for j in range(low,high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]       #make pivot element, such that to left of pivot, elements are all small
    return i+1                                      #and to right of pivot, elements are greater than pivot

    
def quicksort(arr,low,high):
    
    if low < high:
        p = partition(arr,low,high)
        quicksort(arr,low,p-1)                  #recursively apply quicksort for left-side 
        quicksort(arr,p+1,high)                 #recursively apply quicksort for right-side
            
    return arr
    

#driver-code
arr = [5,3,7,9,2,10]
print(quicksort(arr,0,len(arr)-1))
