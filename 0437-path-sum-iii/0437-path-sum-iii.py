# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        count = 0
        sam = 0
        def dfs(root):
            nonlocal sam, count
            if root is None:
                return 0
            sam+=root.val
            if sam ==targetSum:
                count+=1
            dfs(root.left)
            dfs(root.right)
            sam-=root.val
        
        def traverse_dfs(root):
            if root is None:
                return 
            dfs(root)
            traverse_dfs(root.left)
            traverse_dfs(root.right)

        traverse_dfs(root)
        return count



