"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return
        
        oldToCopy = {}

        curr = head
        while curr != None:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr != None:
            copy = oldToCopy[curr]
            if curr.random: copy.random = oldToCopy[curr.random]
            else: copy.random = None
            if curr.next: copy.next = oldToCopy[curr.next]
            else: copy.next = None
            curr = curr.next

        return oldToCopy[head]