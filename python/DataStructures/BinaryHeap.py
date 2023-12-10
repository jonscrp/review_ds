
# Run time 
# Build Heap = O(n)
# max_heapify() = O(logn)
# max() = O(1)s
# inser() = O(logn)
# deleteMax() = O(logn)
# heapsort() = O(nlogn)

# parent() = O(1)
# left() = O(1)
# right() = O(1)

class BinaryHeap():
    
    def __BinaryHeap__(self, A):
        self.heap_size = 0
        self.A= A

    def parent(self,i):
        return i//2
    
    def left(self,i):
        return 2*i
    
    def right(self, i):
        return 2*i + 1
    
    def exchange(self, i, j):
        tmp = self.A[i]
        self.A[i]  = self.A[j]
        self.A[j] = tmp

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest  = i
        if (l <= self.heap_size and self.A[l] > self.A[i]):
            largest = l
        
        if(r <= self.heap_size and self.A[r]  > self.A[largest]):
            largest = r

        if(largest != i):
            self.exchange(i,largest)
            self.max_heapify(largest)


    def insert():
        pass

    def max():
        pass

    def isEmpty(self):
        return self.heap_size == 0

    def buildHeap(self):
        self.heap_size = len(self.A)
        for i in range(self.A.heap_size//2, -1,-1):
            self.max_heapify(i)



