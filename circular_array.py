
#circular array

def circular(arr,i):
    a = []
    l = len(arr)
    for i in range(i,i+l):
        a.append(arr[i%l])
    
    return a

    
#driver code
a = [1,2,3,4,5,6]
i = 4
print(circular(a,i))