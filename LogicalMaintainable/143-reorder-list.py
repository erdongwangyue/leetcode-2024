# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # slow, fast = ?, ?
        # while ? 
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        p1, p2 = head, prev
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next
        


        