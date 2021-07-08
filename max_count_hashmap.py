
#finding max element using hashmap

a = [12,14,16,12,14,16,12,17]
dict = {}
l = len(a)
count_max = 0
maxvalue_index = 0


for i in range(l):
    if a[i] in dict:
        dict[a[i]] = dict[a[i]] + 1         #initialse the count by 1 for the element
    else:
        dict[a[i]] = 1              #initialse count for the num
        


for k in dict:
    maxi = dict[k]                  #gets frequency of the element
    if maxi>= count_max:
        count_max = maxi            #updates the max frequency
        maxvalue_index = k          #element with max count
        
print(maxvalue_index)

