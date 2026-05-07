class ListNode:
    def __init__(self, val, next_node):
        self.val = val
        self.next_node = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1, None)
        self.tail = self.head

    def get(self, index: int) -> int:
        if self.head.next_node==None or (self.head==self.tail and index>0):
            return -1
        curr = self.head
        for i in range(index):
            if not curr:
                return -1
            curr = curr.next_node
        return curr.val if curr!= None else -1

    def insertHead(self, val: int) -> None:
        if self.head.next_node == None:
            self.head.val = val
            self.head.next_node = self.tail
            print("hello")
        elif self.head==self.tail:
            self.head = ListNode(val,self.tail)
            self.tail.next_node = None
            print("hello")
        else:
            node = ListNode(val, self.head)
            self.head = node

    def insertTail(self, val: int) -> None:
        if self.head.next_node==None:
            self.head.next_node = self.tail
            self.tail.val = val
        else:
            node = ListNode(val,None)
            self.tail.next_node = node
            self.tail = node

    def remove(self, index: int) -> bool:
        if self.head.next_node == None:
            return False
        elif self.head==self.tail:
            if index>0:
                return False
            self.head.next_node = None
            self.tail = self.head
            print(self.getValues())
            return True
        elif index==0:
            if self.head.next_node.next_node == None:
                self.head.next_node = self.tail
                self.tail = self.head
            else:
                self.head = self.head.next_node
            return True
        curr = self.head
        for i in range(index-1):
            curr = curr.next_node
        if not curr.next_node.next_node:
            curr.next_node=None
            return True
        curr.next_node = curr.next_node.next_node
        return True

    def getValues(self) -> List[int]:
        if self.head.next_node == None:
            return []
        elif self.head == self.tail:
            return [self.head.val]
        curr = self.head
        vals = []
        while curr!=None:
            vals+=[curr.val]
            curr = curr.next_node
        return vals
