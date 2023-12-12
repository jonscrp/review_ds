
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

    def __init__(self, maxN):
        self.N = 0
        self.pq = [0]*(maxN +  1)

    # Parent
    def parent(self,i):
        return i//2
    

    # Left Child
    def left(self,i):
        return 2*i
    

    # Right Child
    def right(self, i):
        return 2*i + 1
    

    # Helper functions 
    def less(self, i,j):
        return self.pq[i] < self.pq[j]
    

    def exch(self, i ,j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t


    def swim(self, k):
        while( k > 1 and self.less(k//2, k)):
            self.exch(k//2, k)
            k = k//2


    def sink (self, k):
        while 2*k <= self.N:
            j = 2*k
            if(j < self.N  and self.less(j, j+1)):
                j = j + 1
            self.exch(k,j)
            k = j


    def exchange(self, i, j):
        tmp = self.pq[i]
        self.pq[i]  = self.A[j]
        self.pq[j] = tmp


    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest  = i
        if (l <= self.N and self.pq[l] > self.pq[i]):
            largest = l
        
        if(r <= self.N and self.pq[r]  > self.pq[largest]):
            largest = r

        if(largest != i):
            self.exchange(i,largest)
            self.max_heapify(largest)


    # add it to the end of the heap(array)
    def insert(self, v):
        self.N = self.N + 1
        self.pq[self.N] =  v
        self.swim(self.N)


    def max(self):
        if self.isEmpty(): 
            raise Exception("Heap is empty")
        else:
            return self.pq[1]


    # swap the root with the last element 
    # and sink root 
    def delMax(self):
        max = self.pq[1] 
        self.exch(1, self.N)
        self.N = self.N - 1
        self.pq[self.N + 1] = None
        self.sink(1)
        return max
        

    def isEmpty(self):
        return self.N == 0
    
    def traverse(self):
        for v in self.pq:
            print(v)

    def last(self):
        return self.pq[self.N]





heap = BinaryHeap(10)

heap.insert(9)
heap.insert(10)
heap.insert(3)
heap.insert(-4)
heap.insert(0)
heap.insert(9)
heap.insert(99)
heap.insert(100)
heap.insert(-45)
heap.insert(8)

#print(heap.max())
heap.traverse()

# remove max 
heap.delMax()

print("checking heap after deletion")
print("New Max:", heap.max())
print("last node: ", heap.last())
print("Heap after deleting max")
heap.traverse()


