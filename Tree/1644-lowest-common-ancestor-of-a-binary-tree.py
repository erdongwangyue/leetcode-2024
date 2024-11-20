# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # input to dfs()? root, p, q. output? node
        # base case
        # what to do after base case?
        q_found = False
        p_found = False
        
        def dfs(root, p, q):
            nonlocal p_found, q_found, res
            if not root:
                return None
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)
            if root == p or root == q:
                if p.val == root.val:
                    p_found = True
                if q.val == root.val:
                    q_found = True
                return root
            if l and r:
                return root
            else:
                return l or r
        res = dfs(root, p, q) 
        return res if q_found and p_found else None
            
