
# LIFO principle
# Runtime
# length()  : O(1)
# isEmpty() : O(1)
# push()    : O(1)
# pop()     :  O(1)

import LinkList
class Stack:

    def __init__(self):
        self.ll = LinkList.SingleLinkList()

    def length(self):
        return len(self.ll)
    
    def isEmpty(self):
        return len(self.ll)

    def push(self, item):
        self.ll.prepending(item)

    def pop(self):
        return self.ll.deleteFirst()





    
    



