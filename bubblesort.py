
#Bubble Sort Algorithm

def bubblesort(arr):
    l = len(arr)
    
    for i in range(l-1):
        for j in range(0,l-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

arr = [5, 6, 2 ,6, 9, 0, -1]
sort = bubblesort(arr)
print(sort)
