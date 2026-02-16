# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def sortedMerge(head1, head2):
    new_list = ListNode()
    head = new_list


    while(head1 != None and head2 != None):
        if(head1.val < head2.val):
            new_list.next = head1
            head1 = head1.next
        else:
            new_list.next = head2
            head2 = head2.next
        new_list = new_list.next

    if(head1 is not None):
        new_list.next = head1
    elif(head2 is not None):
        new_list.next = head2

    return head.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists) < 1): return ListNode().next

        initial_list = lists.pop(0)

        while(initial_list == None and len(lists) > 0):
            initial_list = lists.pop(0)

        if(len(lists) == 0 and initial_list == None): return initial_list


        while (lists != []):
            next_list = lists.pop(0)

            initial_list = sortedMerge(initial_list, next_list)


        return initial_list