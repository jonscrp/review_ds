
# LinkList vs ArrayList implementation
# Pros:
# A linklist allows us to update(insert or remove nodes) in constant time
# Uses space more efficiently

# Cons:
# Indexing is not available as in Arrays and can take up to O(n) to get to an element

class ListNode():
    def __init__(self, position, data):
            self.positon = position
            self.data = position
            self.next = None
            self.previous = None


class DoublyLinkList:
    def __init__(self):
        self.size = 0 
        self.head = None
        self.trailer = None

    def __len__(self):
        return self.size

    def first(self):
        if self.head is None:
            print("List is empty")
        return self.head
    
    def last(self):
        if self.trailer is None:
            print("List is empty")
        return self.trailer

    def addItem(self, position, item):
        #print(position, item)
        if(self.size == 0):
            self.head == ListNode(position, item )
            self.trailer = self.head
            self.size = self.size + 1
        else:
            obj = ListNode(position, item)
            curNode = self.head
            while curNode  != self.trailer:
                if (curNode.position <= position):
                    self.insertBefore(curNode,obj)
                    self.size = self.size + 1
                    return
            print(self.trailer)
            self.trailer.next = obj 
            obj.previous = self.trailer
            self.traile = obj
            print(self.trailer.position)
            self.size = self.size + 1

    def traverse(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next  

    def before(self, curNode):
        return curNode.previos
       
        
    def after(self, curNode):
        return curNode.next

    def insertBefore(self, curNode, e):
        e.previous = curNode.previous
        e.next = curNode
        curNode.previous = e
           
    def inserAfter(self, curNode, e):
        e.previous = curNode
        e.next = curNode.next
        curNode.next = e
 
    def remove(self, p):
        curNode = self.find(p)
        (curNode.previous).next = curNode.next
        (curNode.next).previos = curNode.previous
        curNode.next = None
        curNode.previos = None 

# helper functions
    def findP(self, p):
        curNode = self.head
        while curNode is not None:
            if( curNode.position == p):
                return curNode
            curNode = curNode.next
        return None



mo = DoublyLinkList()

mo.addItem(4, 9)
mo.addItem(2, 2)
mo.addItem(1, 54)
mo.addItem(23, 3)
mo.addItem(4, 5)
mo.traverse()


        



