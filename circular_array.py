
#circular array

def circular(arr,n):
    a = []
    l = len(arr)
    for i in range(n,n+l):                      #can be from n-1 to n-1+1 depending on the question
         a.append(arr[i%l])
    
    return a

    
#driver code
a = [1,2,3,4,5,6]
n = 2
print(circular(a,n))
