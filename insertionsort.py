
def insertionSort(arr):
    for i in range(1, len(arr)):
        insert = arr[i]
        j = i - 1
        while j>=0 and insert < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1]=insert
            
            
n = int(input("Enter length of list: "))
arr = []
for i in range(n):
    s = int(input())
    arr.append(s)
print("The List Entered: ",arr)

insertionSort(arr)
print("The Sorted List: ",arr)
