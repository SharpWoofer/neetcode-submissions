class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head == None: return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr == None: return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if index == 0:
            if not self.head: return False
            if not self.head.next:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return True
        
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
            # Prev index is not valid to remove
            if curr == None: return False

        # Is the curr index valid to remove?
        if curr.next == None: return False
        else:
            if curr.next.next:
                curr.next = curr.next.next
            else:
                curr.next = None
                self.tail = curr
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr != None:
            res.append(curr.val)
            curr = curr.next
        return res