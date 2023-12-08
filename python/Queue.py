import LinkList

class Queue:
    
    def __init__(self):
        self.ll = LinkList.SingleLinkList()

    def length(self):
        return len(self.ll)
    
    def getHead(self):
        return self.ll.getHead()

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

