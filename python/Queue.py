import LinkList

# FIFO principle
# Runtime of methods
# length() : O(1)
# enque()  : O(1)
# deque()  : O(1)
# length() : O(1)

class Queue:
    
    def __init__(self):
        self.ll = LinkList.SingleLinkList()

    def length(self):
        return len(self.ll)
    
    def isEmpty(self):
        return len(self.ll == 0)
    
    def enque(self, item):
        self.ll.addLast(item)

    def dequeue(self):
        return self.ll.deleteFirst()


u = Queue()

u.enque(5)
u.enque(9)
u.enque(10)
u.enque(-34)


print(u.dequeue())
print(u.dequeue())
print(u.dequeue())
print(u.dequeue())
print(u.dequeue())
print(u.dequeue())

