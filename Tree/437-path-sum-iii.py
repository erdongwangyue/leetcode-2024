class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # What to pay attention to when init prefix sum map?
        # in dfs, what the order is after base case?
        # what the logic is to update res?
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Dictionary to store prefix sums
        res = 0
        
        def dfs(node, currSum):
            nonlocal res
            if not node:
                return
            currSum += node.val
            res += prefix_sums[currSum - targetSum]
            prefix_sums[currSum] += 1
            dfs(node.left, currSum)
            dfs(node.right, currSum)
            prefix_sums[currSum] -= 1  # Backtrack
            
        dfs(root, 0)
        return res
