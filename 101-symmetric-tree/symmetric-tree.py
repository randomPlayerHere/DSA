# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        check1 = self.check(root1.left, root2.right)
        check2 = self.check(root1.right, root2.left)
        return check1 and check2

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)
        