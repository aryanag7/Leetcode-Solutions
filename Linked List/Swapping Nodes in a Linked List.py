# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr=[]
        while head is not None:
            arr.append(head.val)
            head=head.next
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        dummy=ListNode(0)
        temp=dummy
        for i in arr:
            temp.next=ListNode(i)
            temp=temp.next
        return dummy.next
      
        
