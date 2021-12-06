''' Bubblesort give a time complexity of O(n^2) in worst case and average case, 
in best-case that is when an array is already sorted it gives O(n).  '''


def bubblesort(arr):
    
    for i in range(len(arr)-1):                         #run a loop from index 0 to n-1 - counts no. of pass
        sort = False                                    #sort variable used to check if array is sorted, so that it can stop the loop
                                            
        for j in range(len(arr)-1):
            
            if arr[j+1] < arr[j]:                       #comparison based algorithm - compares between elements
                arr[j], arr[j+1] = arr[j+1], arr[j]         #swaps elements which are not in proper order
                
                sort = True                             #alters sort - variable to True                    
            
    if sort == False:                                   #to-check if array has been sorted or not and terminate the sorting process. 
        return arr
    
    
#user-code
array = [7,9,3,1,2,6]                   #unsorted - input array
print(bubblesort(array))                #call the function bubblesort - also prints sorted array
    
