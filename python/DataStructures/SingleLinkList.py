class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Runtime 
# __len__() = O(1)
# traversal() = O(n)
# prepending() = O(1)
# addLast() = O(1) // this is achieved with the addition of a the "last" refence variable
# deleteFirst() =  O(1)
# deleteItem()  =  O(n)

# Note: n represents the number of elements in the list
class SingleLinkList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def traversal(self):
        if self.size == 0:
            return
        
        curNode = self.head
        while curNode is not None:
            print (curNode.data)
            curNode = curNode.next


    # adding elements to the front
    def prepending(self, item):
        newNode = ListNode(item)
        newNode.next = self.head
        self.head = newNode
        self.size = self.size + 1

    def addLast(self, item):
        newNode = ListNode(item)
        if self.size == 0:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size = self.size + 1


    def deleteFirst(self):
        if(self.size == 0):
            return "Empty"
        else:
            tmp = self.head.data
            self.head = self.head.next
            self.size = self.size - 1
            return tmp 
    
        
    def deleteItem(self, item):
        if self.size == 0:
            return
        
        curNode = self.head
        if(curNode.data == k): 
            self.head = self.head.next
           
            self.size = self.size - 1
            return
       
        while curNode.next != None:
            if curNode.next.data == item:
                curNode.next = curNode.next.next 
                self.size = self.size - 1 
                break
            curNode = curNode.next
    



