# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        count = 0
        curr = 0
        mp = {0:1}
        def dfs(root):
            nonlocal curr, count
            if root is None:
                return
            curr+=root.val
            count += mp.get(curr-targetSum, 0)
            mp[curr] = mp.get(curr, 0) +1
            dfs(root.left)
            dfs(root.right)
            mp[curr]-=1
            curr -= root.val
        dfs(root)
        return count

