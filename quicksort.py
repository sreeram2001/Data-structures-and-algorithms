#Quicksort Algorithm

def partition(l,h,arr):
    pivot = arr[h]
    i = l-1
    
    for j in range(l,h):
        if arr[j]<=pivot:
            i = i + 1
            arr[i], arr[j] = arr[j],arr[i]
        
    arr[h], arr[i+1] = arr[i+1], arr[h]
    return i+1
        
        
def quicksort(l,h,arr):
    if l<h:
        par = partition(l,h,arr)
        quicksort(0,par-1,arr)
        quicksort(par+1,h,arr)
        
    return array

array = [10, 7, 8, 9, 1, 5]
val = quicksort(0, len(array) - 1, array)
print(val)
