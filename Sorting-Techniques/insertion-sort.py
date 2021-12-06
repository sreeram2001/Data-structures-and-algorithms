''' Insertionsort gives a time complexity of O(n^2) in worst case and average case, 
in best-case that is when an array is almost sorted it gives O(n).  
In insertionsort which traverse through the array and elements are seqeuentially compared with each other
and arranged into its proper position'''




def insertionsort(arr):
    for i in range(len(arr)):                       #loop through the array
        j = i
        temp = arr[i]                               #the value to be inserted
        
        while arr[j] < arr[j-1] and j > 0:              #keep swapping until value to be inserted is less than elements
            arr[j-1], arr[j] = arr[j], arr[j-1]         
            j = j - 1                                   #iterator
            
        arr[j] = temp
        
    return arr
            

    
    
#user-code
array = [7,9,3,1,2,6]                   #unsorted - input array
print(insertionsort(array))                #call the function bubblesort - also prints sorted array
