
#circular array

def circular(arr,i):
    a = []
    l = len(arr)
    for i in range(i-1,i-1+l):
        a.append(arr[i%l])
    
    return a

    
#driver code
a = [1,2,3,4,5,6]
i = 2
print(circular(a,i))