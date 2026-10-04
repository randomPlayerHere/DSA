# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result = 0
        def dfs(root,hv):
            nonlocal result
            if root is None:
                return
            if root.val >=hv:
                result+=1
                hv = max(root.val, hv)
            if root.left:
                dfs(root.left, hv)
            if root.right:
                dfs(root.right, hv)

        dfs(root, float('-inf'))
        return result
            
            
            
        