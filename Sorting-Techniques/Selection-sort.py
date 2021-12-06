''' Selection Sort is a sorting technique where the idea is to divide the array into two parts, sorted and unsorted.
We find the minimum element in the array and swap it with the left most element in the array, Now the leftmost element
becomes a part of sorted side and the rest of the array is unsorted. We repeat this Process until last index.

Selectionsort gives time complexity of O(n^2)  in all cases. The main work in Selectionsort is to find the index of 
the minimum element in the unsorted part of the array and push it to the leftmost index.'''



def minimum_index(i,arr):
    mini = i        
    
    for j in range(i+1,len(arr)):                           #traverse through the array, to find the minimum element
        if arr[j] < arr[mini]:
            mini = j
            
    return mini                                             #return the index of minimum element to be swapped to left-most side
    

def selectionsort(arr):
    for i in range(len(arr)):                                   #traverse from index 0 - n
        min_index = minimum_index(i,arr)                        #find index of element with minimum value
        
        if i != min_index:                                      #if minimum index is not same as current index, then swap
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
            
    return arr                                                  #return the sorted-array
        

    
#user-code
array = [7,9,3,1,2,6]                   #unsorted - input array
print(selectionsort(array))                #call the function bubblesort - also prints sorted array
