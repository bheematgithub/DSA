# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        
        def help(node,ans,lvl):
            if not node :
                return
            if lvl==len(ans):
                ans.append(node.val)
            if node.right:
                help(node.right, ans, lvl+1)
            if node.left:
                help(node.left, ans, lvl+1)
                
        help(root,res,0)
        return res
