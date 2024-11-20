# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, target):
            if not node:
                return False
            if node.val == target:
                return True
            path.append("L")
            left = dfs(node.left, path, target)
            if left: 
                return True
            path.pop()
            path.append("R")
            right = dfs(node.right, path, target)
            if right: return True
            path.pop()
            return False
        
        start_path = []
        dfs(root, start_path, startValue)
        dest_path = []
        dfs(root, dest_path, destValue)
        i = 0
        while i < min(len(start_path), len(dest_path)):
            if start_path[i] == dest_path[i]:
                i += 1
            else:
                break
        return "".join(["U"] * len(start_path[i:]) + dest_path[i:])