# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        q = deque([(root, 0, 0)])
        while q:
            curr, r, c = q.popleft()
            if curr:
                q.append([curr.left, r + 1, c - 1])
                q.append([curr.right, r + 1, c + 1])
                columns[c].append([r, curr.val])
        sorted_columns = sorted(columns.items())
        res = []
        for _, values in sorted_columns:
            res.append([])
            for _, val in sorted(values):
                res[-1].append(val)
        return res