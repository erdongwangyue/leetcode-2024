# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # res += what?
        res = 0
        def dfs(root):
            if not root:
                return [0, 0] # number of coins, size
            lCoins, lSize = dfs(root.left)
            rCoins, rSize = dfs(root.right)
            coins = root.val + lCoins + rCoins
            size = lSize + rSize + 1
            nonlocal res
            res += abs(size - coins)
            return (coins, size)
        dfs(root)
        return res