# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        R = head
        for _ in range(n):
            R = R.next
        
        dummy = ListNode(0, head)
        L = dummy

        while R != None:
            R = R.next
            L = L.next

        L.next = L.next.next
        return dummy.next