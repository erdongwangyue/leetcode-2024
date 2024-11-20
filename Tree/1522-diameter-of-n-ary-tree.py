"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res = 0
        def dfs(root):
            if not root:
                return 0
            nonlocal res
            max1, max2 = 0, 0
            for nei in root.children:
                neiRes = 1 + dfs(nei)
                if neiRes > max1:
                    max1, max2 = neiRes, max1
                elif neiRes > max2:
                    max2 = neiRes
            res = max(res, max1 + max2)
            # not 1 + max1
            return max1
        dfs(root)
        return res