
#MERGE - INTERVALS

arr = [[1,3], [2,4], [5,7], [6,8]]

arr.sort(key=lambda x:x[0])
merge = []                      #merged-values
lower = -999999999
upper = -999999999

for i in range(len(arr)):
    item = arr[i]
    
    if item[0] > upper:
        if i != 0:
            merge.append([lower, upper])
            

        lower = item[0]
        upper = item[1]
            
    else:
        if item[1] > upper:
            upper = item[1]
            
    print(lower,upper)
  
            
if upper != -999999999 and [lower,upper] not in merge:
    merge.append([lower, upper])
    
print(merge)
print(arr)
