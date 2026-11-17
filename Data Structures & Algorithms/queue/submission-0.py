class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:
        if self.isEmpty(): 
            self.head = ListNode(value)
            self.tail = self.head
        else:
            added_node = ListNode(value)
            self.tail.next = added_node
            added_node.prev = self.tail
            self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        if self.isEmpty(): 
            self.head = ListNode(value)
            self.tail = self.head
        else:
            added_node = ListNode(value)
            self.head.prev = added_node
            added_node.next = self.head
            self.head = self.head.prev

    def pop(self) -> int:
        if self.isEmpty(): return -1
        if self.head == self.tail:
            removed_node = self.tail
            self.tail = None
            self.head = None
            return removed_node.val
        removed_node = self.tail
        self.tail = self.tail.prev
        removed_node.prev = None
        self.tail.next = None
        return removed_node.val


    def popleft(self) -> int:
        if self.isEmpty(): return -1
        if self.head == self.tail:
            removed_node = self.tail
            self.tail = None
            self.head = None
            return removed_node.val
        removed_node = self.head
        self.head = self.head.next
        self.head.prev = None
        removed_node.next = None
        return removed_node.val