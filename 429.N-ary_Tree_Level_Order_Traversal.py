"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root :
            return
        res=[]
        que=[root]

        while que:
            lsz=len(que)
            lvl=[]
            for _ in range(lsz):
                node= que.pop(0)
                lvl.append(node.val)
                if node.children:
                    que.extend(node.children)
            res.append(lvl)
        return res
        
