# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return
        el=[]
        for i in lists:
            while i:
                el.append(i.val)
                i=i.next
        el.sort()
        res=ListNode(0)
        cur=res
        for i in el:
            cur.next=ListNode(i)
            cur=cur.next
        return res.next
