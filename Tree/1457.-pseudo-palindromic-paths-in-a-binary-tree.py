# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # in dfs oddChange, count, odd
        # update res when not left and not right
        res = 0
        currCount = defaultdict(int)
        odd = 0
        def dfs(root):
            if not root:
                return
            curr = root.val
            nonlocal odd
            nonlocal res
            oddChange = 1 if currCount[curr] % 2 == 0 else -1 # else 0
            odd += oddChange
            currCount[curr] += 1
            if not root.left and not root.right:
                res += 1 if odd <= 1 else 0
            dfs(root.left)
            dfs(root.right)
            odd -= oddChange
            currCount[curr] -= 1

        dfs(root)
        return res

