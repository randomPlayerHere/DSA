# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sam = 0
        def dfs(root):
            nonlocal sam
            if root is None:
                return 0
            dfs(root.right)
            temp = root.val
            root.val += sam
            sam +=temp
            dfs(root.left)
            return root.val
        dfs(root)
        return root