# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        queue = deque([root])
        result = []
        def dfs(root):
            if root is None:
                return None
            if root.val in to_delete:
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root
        
        while queue:
            node = queue.popleft()
            if node.val in to_delete:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                continue
            result.append(node)
            dfs(node)
        return result
