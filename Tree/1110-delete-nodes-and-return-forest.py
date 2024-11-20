# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # to_delete, res: set, set
        # dfs, input node, output node
        to_delete = set(to_delete)
        res = set([root])
        def dfs(root):
            if not root:
                return None
            result = root
            # root.val not root
            if root.val in to_delete:
                result = None
                res.discard(root)
                if root.left: res.add(root.left)
                if root.right: res.add(root.right)
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return result
        dfs(root)
        return list(res)
            