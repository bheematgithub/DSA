# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        n=0
        hed=head
        while hed:
            n+=1
            hed=hed.next
        max_=0
        twin={}
        c=0
        while head:
            v=n-1-c
            if v in twin:
                max_=max((head.val+twin[v]),max_)
            twin[c]=head.val
            c+=1
            head=head.next
        return max_

