# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mp = {}
        result = []

        def dfs(root):
            if root is None:
                return None
            key = (root.val, dfs(root.left), dfs(root.right))
            mp[key] = mp.get(key,0) +1
            if mp[key] == 2:
                result.append(root)
            return key
        dfs(root)
        return result
