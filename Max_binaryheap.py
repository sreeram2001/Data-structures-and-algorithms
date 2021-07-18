
class maxHeap:
    def __init__(self):
        self.heap = []
        
    
    def parent(self, i):
        return int((i-1)/2)
        
    def left_child(self, i):
        return 2*i+1
        
    def right_child(self, i):
        return 2*i+2
        
        
    
    def has_parent(self,i):
        return self.parent(i)>=0
        
    def has_left_child(self,i):
        return self.left_child(i) < len(self.heap)
        
    def has_right_child(self,i):
        return self.right_child(i) < len(self.heap)
        
        

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
        
        
        
        
  
    def insert(self, key):
        self.heap.append(key)
        self.heapifyup(len(self.heap)-1)
        
        
    def heapifyup(self,i):
        while (self.has_parent(i) and self.heap[i] > self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)
        
        
    #deleting max element
    
    
    
    def delete(self):
        if len(self.heap)==0:
            return -1
        last_index = len(self.heap)-1
        self.swap(0, last_index)
        root = self.heap.pop()
        self.heapifydown(0)
        return root
        
        
    def heapifydown(self, i):
        while(self.has_left_child(i)):
            max_child_index = self.get_max_child(i)
            
            if max_child_index == -1:
                break
            if(self.heap[i] < self.heap[max_child_index]):
                self.swap(i, max_child_index)
                
            else:
                break
        
        
    def get_max_child(self, i):
        if (self.has_left_child(i)):
            left = self.left_child(i)
            if(self.has_right_child(i)):
                right = self.right_child(i)
                
                if(self.heap[left] > self.heap[right]):
                    return left
                else:
                    return right
        else:
            return -1
                    
        
        
    #print heap    
    def viewheap(self):
        if self.heap:
            return self.heap
       
        
    #get max element    
    def get_max(self):
        return self.heap[0]


heap = maxHeap()
heap.insert(45)
heap.insert(99)
heap.insert(63)
heap.insert(35)
heap.insert(29)
heap.insert(57)


heap.insert(70)


print(heap.viewheap())





print("Maximum Element Is: ",heap.get_max())
print(heap.viewheap())


print("Deleted Element: ",heap.delete())
print("Heap After Deletion: ")
print(heap.viewheap())
    
        
    



