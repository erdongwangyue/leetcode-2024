# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))
        dummy = ListNode()
        curr = dummy
        while heap:
            new = heapq.heappop(heap)
            node = new.node
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, HeapNode(node.next))
        return dummy.next
