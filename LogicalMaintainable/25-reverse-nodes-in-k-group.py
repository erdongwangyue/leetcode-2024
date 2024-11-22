# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                curr.next, prev, curr = prev, curr, curr.next
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            # groupPrev, groupPrev.next = groupPrev.next, kth
        return dummy.next
    def getKth(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
            
        