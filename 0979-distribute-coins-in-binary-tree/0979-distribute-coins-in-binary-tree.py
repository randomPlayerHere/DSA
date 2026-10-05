# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if root is None:
                return 0
            lv = dfs(root.left)
            rv = dfs(root.right)
            excess = lv+rv+root.val-1
            count += abs(excess)
            return excess
        dfs(root)
    
        return count
