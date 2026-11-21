# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        elif list2 == None: return list1
        elif list1.val < list2.val:
            curr = list1
            list1 = list1.next
        else:
            curr = list2
            list2 = list2.next

        head = curr
        curr.next = self.mergeTwoLists(list1, list2)
        return head