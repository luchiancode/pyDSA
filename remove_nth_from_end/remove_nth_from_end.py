# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while(curr != None):
            curr = curr.next
            length+=1
        
        item_position = length - n
        curr = head
        previous = None

        if(length == 2 and n == 1):
            head.next = None
        if(length == 2 and n == 2):
            head = head.next


        if(length > 2):
            for i in range(item_position):
                if(i == item_position - 1):
                    previous = curr
                curr = curr.next
            
           
            if (item_position == 0):
                head = head.next
            elif(item_position == length):
                curr.next = None
            elif(curr.next != None):    
                previous.next = curr.next 
            else: previous.next = None
            curr = None

        if(length == 1): head = None

        return head


        