
''' Merge-sort has a time-complexity of O(nlogn) in all cases. It is a divide and conquer technique and
also a comparison-based algorithm. Merge sort repeatedly breaks down a list into several sublists until each 
sublist consists of a single element and merging those sublists in a manner that results into a sorted list.'''

''' Split the array into two, make a recursive call and merge the results. Divide the unsorted list into sublist of 
each one element, and repeatedly merge the sublists in a sorted manner until there is only one sublists remaining.'''


def mergesort(arr):
    
    if len(arr) > 1:
        
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        
        mergesort(l)
        mergesort(r)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i = i + 1
            else:
                arr[k] = r[j]
                j = j + 1
                
            k = k + 1
            
        
        while i < len(l):
            arr[k] = l[i]
            i = i + 1
            k = k + 1
            
        while j < len(r):
            arr[k] = r[j]
            k = k + 1
            j = j + 1
            
    
    return arr
      
    
#user-code
array = [7,9,3,1,2,6]                   #unsorted - input array
print(mergesort(array))                #call the function - also prints sorted array
