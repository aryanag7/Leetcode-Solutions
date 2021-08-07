# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p=head
        q=head
        while q is not None and q.next is not None:
            p=p.next
            q=q.next.next
        head=p
        return head
      
      
      
        p=head
        q=head
        while q.next is not None and q.next.next is not None:
            p=p.next
            q=q.next.next
        head=p.next
        return head
            
        
        
