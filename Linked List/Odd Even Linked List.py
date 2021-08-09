# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        oddhead=None
        oddtail=None
        evenhead=None
        eventail=None
        i=1
        while i>0 and head is not None:
            if i%2==0:
                if eventail is None:
                    evenhead=head
                    eventail=head
                else:
                    eventail.next=head
                    eventail=eventail.next
                
            else:
                if oddtail is None:
                    oddhead=head
                    oddtail=head
                else:
                    oddtail.next=head
                    oddtail=oddtail.next
                
            head=head.next
            i=i+1
        if oddtail is None:
            eventail.next=None
            return evenhead
        elif eventail is None:
            oddtail.next=None
            return oddhead
        else:
            oddtail.next=None
            eventail.next=None
            oddtail.next=evenhead
            return oddhead
  
        
