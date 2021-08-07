# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next                 O(N+M) WITH CONSTANT SPACE
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val>l2.val:
            temp=ListNode()
            temp=l1
            l1=l2
            l2=temp
        ans=ListNode()
        ans=l1
        while l1 is not None and l2 is not None:
            tomp=None
            while l1 is not None and l1.val<=l2.val:
                tomp=l1
                l1=l1.next
            tomp.next=l2
            temp=ListNode()
            temp=l1
            l1=l2
            l2=temp
            
        
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val 
#         self.next = next                O(N+M) WITH SPACE o(n+m)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)
        temp=dummy
        if l1 is None:
            return l2
        if l2 is None:
            return l1
       
        while l1!=None and l2!=None:
            if l1.val <= l2.val:
                temp.next=l1
                l1=l1.next
               
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        while l1 is not None:
            temp.next=l1
            l1=l1.next
            temp=temp.next
        while l2 is not None:
            temp.next=l2
            l2=l2.next
            temp=temp.next
        return dummy.next
                
        
        
        
