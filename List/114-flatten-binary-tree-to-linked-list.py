class Solution:
    def flatten(self, root: TreeNode) -> None:

        def dfs(root):
            if not root or (not root.left and not root.right):
                return root
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            return rightTail if rightTail else leftTail
        dfs(root)