"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root :
            return
        
        res=[]
        res.append(root.val)
        if root.children:
            for  node in root.children:
                res.extend(self.preorder(node))
        return res
