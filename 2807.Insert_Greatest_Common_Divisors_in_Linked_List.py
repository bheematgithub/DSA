# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res=head
        while head.next:
            el1=head.val
            el2=head.next.val
            while el2:
                el1,el2=el2,el1%el2
            tmp=head.next
            head.next=ListNode(abs(el1))
            head.next.next=tmp
            head=tmp
        return res
