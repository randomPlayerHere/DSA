# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def rightmostNode(root):
            while root.right:
                root=root.right
            return root
        
        curr = root
        inorder = []
        while curr is not None:
            if curr.left is None:
                inorder.append(curr.val)
                curr=curr.right
            else:
                node = rightmostNode(curr.left)
                node.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return inorder

