# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 0-> Not covered, 1-> Convered, 2 -> cameras
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        count = 0
        def recur(root):
            nonlocal count
            if root is None:
                return 1
            lv = recur(root.left)
            rv = recur(root.right)
            if not lv or not rv:
                count+=1
                return 2
            if lv == 2 or rv == 2:
                return 1
            return 0
        check = recur(root)
        if check ==0:
            count+=1
        return count

            
