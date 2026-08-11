# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def rightMost(node):
            while node.right:
                node = node.right
            return node
        
        curr = root
        while curr is not None:
            if curr.left:
                temp = rightMost(curr.left)
                temp.right = curr.right
                curr.right = curr.left
                curr.left = None
                curr=curr.right
            else:
                curr = curr.right
        
        