# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string=""
        p=head
        while p is not None:
            string=string+str(p.val)
            p=p.next
        decimal=int(string,2)
        return decimal
        
        
        
        
        res=0
        while head is not None:
            res=res*2
            res=res+head.val
            head=head.next
        return res
