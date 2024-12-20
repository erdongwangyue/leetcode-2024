# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # what is the value of not_rob?
        # ultimately return what?
        def dfs(node):
            if not node:
                return (0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            
            # If we don't rob this node, we can choose to rob or not to rob its children
            not_rob = max(left) + max(right)
            
            return (rob, not_rob)
        
        return max(dfs(root))
