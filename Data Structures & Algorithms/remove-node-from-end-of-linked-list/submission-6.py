# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None: return
        fast, slow = head, head
        count = 0
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            count += 1
        if fast.next: count = count * 2 + 2
        else: count = count * 2 + 1
        if n > count: return
        index = count - n
        # dummy node method
        dummy = ListNode(0, head)
        slow2 = dummy
        for _ in range(index):
            slow2 = slow2.next
        if not slow2.next.next:
            slow2.next = None
        else:
            slow2.next = slow2.next.next
        return dummy.next