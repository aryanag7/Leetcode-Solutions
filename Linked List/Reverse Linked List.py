# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev=None
        p=head
        while p is not None:
            q=p.next
            p.next=prev
            prev=p
            p=q
        head=prev
        return head
        
        
#         if head is None:
#             return
#         self.reverseList(head.next)
#         print(head.val,end=" ")
        
