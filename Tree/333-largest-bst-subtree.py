# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # What is the input to dfs? What is the output?
        # Ans: node; (is_bst, tree_size, min_of_tree, max_of_tree)
        # Number of base cases: 2
        # order: post
        # recursion logic: 4 condisions with if/elif/else, starting with True results
        if not root:
            return 0
        res = 1

        def dfs(node):
            if not node:
                return (False, 0, -10001, 10001)
            if not node.left and not node.right:
                return (True, 1, node.val, node.val)
            l_is_bst, l_size, l_min, l_max = dfs(node.left)
            r_is_bst, r_size, r_min, r_max = dfs(node.right)
            nonlocal res
            if l_is_bst and r_is_bst and l_max < node.val < r_min:
                cur_size = 1 + l_size + r_size
                res = max(res, cur_size)
                return (True, cur_size, l_min, r_max)
            elif l_is_bst and not node.right and l_max < node.val:
                cur_size = 1 + l_size
                res = max(res, cur_size)
                return (True, cur_size, l_min, node.val)
            elif r_is_bst and not node.left and r_min > node.val:
                cur_size = 1 + r_size
                res = max(res, cur_size)
                return (True, cur_size, node.val, r_max)
            else:
                return (False, 0, -10001, 10001)
        
        dfs(root)
        return res