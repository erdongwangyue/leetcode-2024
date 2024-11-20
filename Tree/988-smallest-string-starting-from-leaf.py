# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # not easy to maintain a global res because it is hard to init res
        res = ""
        def dfs(root, curr):
            if not root:
                return curr
            curr = chr(ord('a') + root.val) + curr
            nonlocal res
            if not root.left and not root.right:
                if res == "":
                    res = curr
                else:
                    res = min(res, curr)
            
            # curr = chr(ord('a') + root.val) + curr
            # # curr = chr(root.val + ord("a")) + curr # str(root.val + ord("a")) + curr
            # if not root.left and not root.right:
            #     return curr
            if root.left:
                dfs(root.left, curr)
            if root.right:
                dfs(root.right, curr)
            # return min(dfs(root.left, curr), dfs(root.right, curr))
        dfs(root, "")
        return res
