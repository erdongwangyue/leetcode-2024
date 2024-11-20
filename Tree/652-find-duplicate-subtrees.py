# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root):
        def dfs(node):
            if not node:
                return ""
            s = ("(" + dfs(node.left) + ")" + str(node.val)
                              + "(" + dfs(node.right) + ")")
            subtrees[s] += 1
            if subtrees[s] == 2:
                res.append(node)
            return s
        subtrees = collections.defaultdict(int)
        res = []
        dfs(root)
        return res
            