"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        def dfs(prev, curr):
            if not curr:
                return prev
            prev.next = curr
            curr.prev = prev
            newCurr = curr.next
            newPrev = dfs(curr, curr.child)
            curr.child = None
            return dfs(newPrev, newCurr)
        dummy = Node(0, None, head, None)
        dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next
