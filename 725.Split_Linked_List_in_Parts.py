# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        root = prev = head
        n=int()
        while head:
            n+=1
            head=head.next

        base,rem = n//k, n%k
        res=[]
        
        for i in range(k):
            res.append(root) if root else res.append(None)
            for i in range(base):
                prev=root
                root=root.next
            if rem>0:
                prev=root
                root=root.next
                rem-=1
            if prev:
                prev.next=None

        return res
