# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def trvl(root,l):
            if not root :
                return
            if not root.left and not root.right:
                l.append(root.val)
            else: 
                trvl(root.left,l)
                trvl(root.right,l)
            return l

        return trvl(root1,l=[]) == trvl(root2,l=[])
