# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = {val: i for i,val in enumerate(inorder)}
        pre = len(postorder) -1
        def dfs(left, right):
            nonlocal pre
            if left>right:
                return None
            rootVal = postorder[pre]
            i = mp[rootVal]
            root = TreeNode(rootVal)
            pre-=1
            root.right= dfs(i+1, right)
            root.left = dfs(left, i-1)
            return root
        return dfs(0,len(inorder)-1)