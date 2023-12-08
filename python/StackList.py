

import LinkList
class Stack:

    def __init__(self):
        self.ll = LinkList.SingleLinkList()

    
    def isEmpty(self):
        return len(self.ll)

    def push(self, item):
        self.ll.prepending(item)


    def pop(self):
        return self.ll.deleteFirst()





    
    



