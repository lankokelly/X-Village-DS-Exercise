class MinHeap:
    def __init__(self):
        self.min_heap_list = []
        self.current_size = 0
        self.big_value = 10000000
    def build_heap(self,unsort_list):
        N = len(unsort_list) // 2  #start check index
        self.current_size  = len(unsort_list) 
        self.min_heap_list =  unsort_list
        for i in range(0,N):  # time of checking
            for n in range (N-1 , -1 , -1): # index of checking from N-1 to 0
                if (len(unsort_list)%2==0 and len(unsort_list)%2!=2):
                    self.min_heap_list.append(self.big_value)  # insert a dummy value
                if(self.min_heap_list[n]>self.min_heap_list[2*n+1] or self.min_heap_list[n]>self.min_heap_list[2*n+2] ):
                    #print(self.min_heap_list[n]) #index=1 值為5 要和index=3,4比
                    minchild_value = min (self.min_heap_list[2*n+1] , self.min_heap_list[2*n+2] )
                    minindex = self.min_heap_list.index(minchild_value)
                    temp = self.min_heap_list[n]
                    self.min_heap_list[n] = self.min_heap_list[minindex]
                    self.min_heap_list[minindex] = temp
        
        if(self.big_value in self.min_heap_list):  # if dummy value in the list, remove it!
            self.min_heap_list.remove(self.big_value)
  
    def insert(self, item):
        self.min_heap_list.append(item)
        self.build_heap(self.min_heap_list)
        
    def del_min(self):
        min_del_value = self.min_heap_list[0]  # reserve the min value so that we can return
        self.min_heap_list[0] = self.big_value  # assign dummy value to list[0]
        self.build_heap(self.min_heap_list)
        if(self.big_value in self.min_heap_list):
            self.min_heap_list.remove(self.big_value) #remove dummy value
        return min_del_value 
    
    def display(self):
        print(self.min_heap_list)

heap = MinHeap()
heap.build_heap([9, 5, 6, 2, 3])
heap.display()

heap.insert(1)
heap.insert(7)
heap.display()

print(heap.del_min())
print(heap.del_min())
heap.display()