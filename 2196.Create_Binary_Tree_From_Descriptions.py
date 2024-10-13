# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hmap , child = {} ,set()

        for i in descriptions:
            prt, cld, lft = i

            if prt not in hmap:
                hmap[prt] = TreeNode(prt)

            if cld not in hmap:
                hmap[cld] = TreeNode(cld)

            if lft:
                hmap[prt].left = hmap[cld]
            else:
                hmap[prt].right = hmap[cld]

            child.add(cld)

        for i in descriptions:
            prt = i[0]
            if prt not in child:
                return hmap[prt]

        return None
