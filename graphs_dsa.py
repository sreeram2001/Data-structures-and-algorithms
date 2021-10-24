#Graph Data Structure
 
#linkedlist of nodes
class llnode:
    def __init__(self,data):
        self.data = data
        self.next = None
         
         
class Graph:
    def __init__(self,vertices):
        self.l = vertices
        self.graph = [None]*self.l      #adjacent-matrix
        
        
    #add-edges
    def add(self,start,end):
        
        node = llnode(start)
        node.next = self.graph[end]
        self.graph[end] = node
        
        node = llnode(end)
        node.next = self.graph[start]
        self.graph[start] = node
        
        
    def network(self):
        for i in range(self.l):
            ele = self.graph[i]
            print(i,end="")
            
            while ele:
                print(" -> {}".format(ele.data),end=" ")
                ele = ele.next
                
            print()
            
                
g = Graph(5)
g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(3,2)
g.add(3,1)
g.add(4,2)
g.network()
    