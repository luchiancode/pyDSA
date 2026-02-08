# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        no1,no2  = 0,0
        while(l1):
            no1 = no1*10+l1.val 
            l1 = l1.next

        while(l2):
            no2 = no2*10+l2.val
            l2=l2.next

        new_number = str(no1+no2)[::-1]
        head = ListNode()
        new_list = head

        for no in new_number:
            new_list.next = ListNode(int(no))
            new_list = new_list.next
            
        return head.next


